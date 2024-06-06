%module Clothoids

// Injected C++ code
%{
#include "clothoids_interface.hh"
%}

%include "std_pair.i"
%include "std_vector.i"
%template() std::pair<double, double>;
%template() std::vector<double>;
%include "GenericContainer.i"

%include "clothoids_interface.hh"
