/*Solve the harmonic ascillator \ddot{x} = -x using Euler's Algorithm*/
#include <iostream>
#include <sstream>
#include <string>
#include <math.h>
using namespace std;


float force(float x){
  return -x;
}
float position_analitical(float time){
  return sin(time);
}
float momentum_analytical(float time){
  return cos(time);
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
  position[0] = x0;
  momentum[0] = p0;
  cout << "Time" << ',' << "Position" << ',' << "Momentum" << ',' << "Position-A" << ',' << "Momentum-A" << endl;
  cout << 0 << ',' << position[0] << ',' << momentum[0] << ',' << position_analitical(0) << ',' << momentum_analytical(0) <<  endl;
  for(int i = 0; i<N_steps-1;i++){
    // Predictor step
    float position_predict = position[i] + step_size * momentum[i];
    float momentum_predict = momentum[i] + step_size * force(position[i]);
    // Compute new force
    float force_predict = force(position_predict);
    // Corrector step
    position[i+1] = position[i] + 0.5 * step_size * (momentum[i] + momentum_predict);
    momentum[i+1] = momentum[i] + 0.5 * step_size * (force(position[i]) + force_predict);
    float t = (i+1)*step_size;
    cout << t << ',' << position[i+1] << ',' << momentum[i+1] << ',' << position_analitical(t) << ',' << momentum_analytical(t) << endl;
  }


  return 0;
}
