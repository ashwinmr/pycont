import numpy as np
import matplotlib.pyplot as plt
import control

def create_pendulum(m,l):
  """ Create a state space pendulum

  Pendulum equations
  l.theta_dot_dot = -g.sin(theta) + F

  Variables:
  theta -> counter clockwise angle [rad]
  l -> length of pendulum [m]
  F -> input force [N]
  g -> gravity [m/s^2]

  States:
  theta
  theta_dot

  Inputs:
  F

  Outputs:
  theta

  """

  # Set constants
  g = 9.81

  A = np.array([[0    , 1],
               [(-g/l), 0]])

  B = np.array([[0],
                [1/(m*l)]])

  C = np.array([[1,0]])

  D = np.array([[0]])

  sys = control.StateSpace(A,B,C,D)

  return sys


def main():

  # Create a state space pendulum

  # Set variables
  m = 1 # Mass
  l = 1 # Length

  sys = create_pendulum(m,l)

  # Impulse response
  t,y = control.impulse_response(sys)

  plt.plot(t,y)
  plt.xlabel('time [s]')
  plt.ylabel('theta [rad]')
  plt.grid(True)
  plt.show()

if __name__ == "__main__":
  main()
