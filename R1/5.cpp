int* r0(int a, int b) {
  int* output; int maxfactors, index = 0; // initializing
  for (int i = a; i < b; i++) { int factors = 0;
    for (int j = 1; j <= i; j++) {if (i%j == 0) {factors++;}} // count factors
    if (factors > maxfactors) { // restart array if more factors, otherwise append
      output = new int[b-a]; output[0] = i; index = 1; maxfactors = factors;
    } else if (factors == maxfactors) {output[index++] = i;}
  }
  output[index] = -1; return output; // append -1 to signify EOF
}
