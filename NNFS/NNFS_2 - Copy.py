{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4.8\n"
     ]
    }
   ],
   "source": [
    "# modeling a single neuron with 3 inputs\n",
    "\n",
    "inputs = [1.0, 2.0, 3.0, 2.5]\n",
    "weights = [0.2, 0.8, -0.5, 1.0]\n",
    "bias = 2 # 1 bias value per neuron, tunable value not associated with  any input\n",
    "\n",
    "output = (inputs[0]*weights[0] +\n",
    "          inputs[1]*weights[1] +\n",
    "          inputs[2]*weights[2] + \n",
    "          inputs[3]*weights[3] + bias)\n",
    "print(output)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
