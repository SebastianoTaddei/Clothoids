#include "Clothoids.hh"
#include <string>
#include <utility>
#include <vector>

namespace clothoids
{

class ClothoidCurve
{
private:
  G2lib::ClothoidCurve clothoid_curve;

public:
  ClothoidCurve(std::string const &name = "") : clothoid_curve{name} {}

  ClothoidCurve(
      double x0, double y0, double theta0, double k, double dk, double L,
      std::string const &name
  )
      : clothoid_curve{x0, y0, theta0, k, dk, L, name}
  {
  }

  void build(double x0, double y0, double theta0, double k, double dk, double L)
  {
    this->clothoid_curve.build(x0, y0, theta0, k, dk, L);
  }

  int build_G1(
      double x0, double y0, double theta0, double x1, double y1, double theta1,
      double tol = 1e-12
  )
  {
    return this->clothoid_curve.build_G1(x0, y0, theta0, x1, y1, theta1, tol);
  }

  double length() { return this->clothoid_curve.length(); }

  std::pair<double, double> eval(double s)
  {
    double x, y;
    this->clothoid_curve.eval(s, x, y);
    return {x, y};
  }
};

class ClothoidList
{
private:
  G2lib::ClothoidList clothoid_list;

public:
  ClothoidList(std::string const &name = "") : clothoid_list{name} {}

  bool build_G1(std::vector<double> const &x, std::vector<double> const &y)
  {
    return this->clothoid_list.build_G1(x.size(), x.data(), y.data());
  }

  double length() { return this->clothoid_list.length(); }

  std::pair<double, double> eval(double s)
  {
    double x, y;
    this->clothoid_list.eval(s, x, y);
    return {x, y};
  }
};

}; // namespace clothoids
