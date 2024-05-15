%module Clothoids

%{
#include "clothoids_interface.hh"
%}

%include "std_pair.i"
%include "std_string.i"
%include "std_vector.i"
%template() std::pair<double, double>;
%template() std::vector<double>;

%include "clothoids_interface.hh"
