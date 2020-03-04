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
      "[9 8 7 6 5 4 3 2 1 0]\n"
     ]
    }
   ],
   "source": [
    "# Создайте numpy array с элементами от числа N до 0 \n",
    "#(например, для N = 10 это будет array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])).\n",
    "\n",
    "import numpy as np\n",
    "N = 10\n",
    "print (np.arange( N - 1, 0 -1 , -1))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[10  0  0  0  0  0  0  0  0  0  0]\n",
      " [ 0  9  0  0  0  0  0  0  0  0  0]\n",
      " [ 0  0  8  0  0  0  0  0  0  0  0]\n",
      " [ 0  0  0  7  0  0  0  0  0  0  0]\n",
      " [ 0  0  0  0  6  0  0  0  0  0  0]\n",
      " [ 0  0  0  0  0  5  0  0  0  0  0]\n",
      " [ 0  0  0  0  0  0  4  0  0  0  0]\n",
      " [ 0  0  0  0  0  0  0  3  0  0  0]\n",
      " [ 0  0  0  0  0  0  0  0  2  0  0]\n",
      " [ 0  0  0  0  0  0  0  0  0  1  0]\n",
      " [ 0  0  0  0  0  0  0  0  0  0  0]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "55"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Создайте диагональную матрицу с элементами от N до 0. Посчитайте сумму ее значений на диагонали.\n",
    "\n",
    "import numpy as np\n",
    "N = 10\n",
    "A = np.diag(np.arange( N, 0-1, -1), k = 0 )\n",
    "print (A)\n",
    "np.sum (np.diagonal (A))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0.46666667,  3.84444444, -5.55555556])"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# (Решите систему уравнений:\n",
    "# 4x + 2y + z = 4\n",
    "# x + 3y = 12\n",
    "# 5y + 4z = -3\n",
    "\n",
    "import numpy as np\n",
    "A = np.array ([[4.,2.,1.],[1., 3., 0.],[0., 5., 4.]])\n",
    "B = np.array ([4., 12., -3.])\n",
    "np.linalg.solve(A, B)"
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
