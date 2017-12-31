#include <PIDController.h>
#include <PIDSource.h>
#include <PIDOutput.h>
#include <Timer.h>
#include <vector>
#include <numeric>
#include <iostream>
#include <fstream>
#include <HAL/HAL.h>

// with period of 50 ms, I get mean = 50 ms, std dev = 21 microseconds
// with period of 10 ms, I get mean = 10 ms, std dev ~ 15 microseconds
// with period of 1 ms, I get mean = 1 ms, std dev ~ 12 microseconds
// with period of 600 us, I get mean = 600 us, std dev ~ 11 microseconds
// with period of 500 us, I get mean = 500 us, std dev ~ 11 microseconds
// with period of 200 us, I get mean = 200 us, std dev ~ 30 microseconds
// with period of 100 us, I get mean = 100 us, std dev ~ 48 microseconds

using namespace frc;

class DerpSource : public PIDSource {
public:
    virtual void setPIDSourceType(PIDSourceType pidSource) {
        m_pidSource = pidSource;
    }

    virtual PIDSourceType GetPIDSourceType() const {
        return m_pidSource;
    }

    virtual double PIDGet() {
        return 1.1;
    }
private:
    PIDSourceType m_pidSource;
};

class DerpOutput : public PIDOutput {
public:
    DerpOutput(std::vector<double> *timings) {
        m_timings = timings;
        m_timer.Start();
    }
    virtual void PIDWrite(double output) {
        double time = m_timer.Get();
        if (output != 0) {
            m_timings->push_back(time);
        }
    }
private:
    Timer m_timer{};
    std::vector<double> *m_timings;
};

// grr, where in library?
double mean(std::vector<double> &timings) {
    double sum = std::accumulate(timings.begin(), timings.end(), 0.0);
    return sum / timings.size();
}

// grr, where in library?
double stdev(std::vector<double> &timings) {
    double _mean = mean(timings);

    std::vector<double> diff(timings.size());
    std::transform(timings.begin(), timings.end(), diff.begin(),
                   std::bind2nd(std::minus<double>(), _mean));
    double sq_sum = std::inner_product(diff.begin(), diff.end(), diff.begin(), 0.0);
    double stdev = std::sqrt(sq_sum / timings.size());

    return stdev;
}

int main() {
    HAL_Initialize(100, HAL_Athena);
    std::vector<double> timings;
    PIDSource *source = new DerpSource();
    DerpOutput *output = new DerpOutput(&timings);
    PIDController *pidController = new PIDController(1, 1, 1, source, output, 0.0002);
    pidController->Enable();

    Wait(10);

    pidController->Disable();

    Wait(2);

    std::vector<double> _timingdiffs(timings.size()); 
    std::adjacent_difference(timings.begin(), timings.end(), _timingdiffs.begin());
    // stupid adjacent_difference, I don't want a non-difference
    auto beg = _timingdiffs.begin();
    if(beg != _timingdiffs.end()) {
        beg++;
    }
    std::vector<double> timingdiffs(beg, _timingdiffs.end());
    double _mean = mean(timingdiffs);
    double _stdev = stdev(timingdiffs);

    std::cout << "mean: " << _mean << std::endl;
    std::cout << "stdev: " << _stdev << std::endl;

    std::ofstream csvFile;
    csvFile.open("timings.csv");
    for(auto it = timings.begin(); it != timings.end(); ++it) {
        csvFile << *it << std::endl;
    }
    csvFile.close();
}
