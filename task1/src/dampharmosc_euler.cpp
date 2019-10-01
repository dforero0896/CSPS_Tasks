/*Solve the harmonic ascillator \ddot{x} = -x using Euler's Algorithm*/
#include <iostream>
#include <sstream>
#include <string>
#include <math.h>
using namespace std;


float force(float x, float p, float gamma){
  return -p*gamma - x;
}
float force_derivative(float x, float p , float gamma, float f){//wrt t
  /* For the undampened here we had the partial derivative wrt x
  We ask for the force so no extra computations are introduced*/
  return -gamma * f - p;
}
float position_analitical(float time, float gamma){
  return sin(time)*exp(-0.5*gamma*time);
}
float momentum_analytical(float time, float gamma){
  return cos(time)*exp(-0.5*gamma*time);
}
int main(int argc, char const *argv[]) {
  if(argc == 1){
    cout << "ERROR: Expected number of steps.\nUSAGE: " << argv[1] << " NSTEPS" << endl;
  }
  float x0 = 0;
  float p0 = 1;
  float total_time = 12.56637061; //Emulate program given by Prof.
  int N_steps = atoi(argv[1]);
  float step_size = total_time/N_steps;
  float position[N_steps];
  float momentum[N_steps];
  float forces[N_steps];
  float gamma = 0.5;
  position[0] = x0;
  momentum[0] = p0;
  forces[0] = force(x0, p0, gamma);
  cout << "Time" << ',' << "Position" << ',' << "Momentum" << ',' << "Position-A" << ',' << "Momentum-A" << endl;
  cout << 0 << ',' << position[0] << ',' << momentum[0] << ',' << position_analitical(0, gamma) << ',' << momentum_analytical(0, gamma) <<  endl;
  for(int i = 0; i<N_steps-1;i++){
    position[i+1] = position[i] + step_size * momentum[i];
    momentum[i+1] = momentum[i] + step_size * force(position[i], momentum[i], gamma);
    forces[i+1] = force(position[i+1], momentum[i+1], gamma);
    float t = (i+1)*step_size;
    cout << t << ',' << position[i+1] << ',' << momentum[i+1] << ',' << position_analitical(t, gamma) << ',' << momentum_analytical(t, gamma) << endl;
  }


  return 0;
}
