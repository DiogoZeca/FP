def pyramidVolume(N):
   """Compute the volume of a pyramid of cubes with N layers."""
   if N <= 0:
      return 0
   vol = N * N + pyramidVolume(N-1)
   return vol

print(pyramidVolume(2))