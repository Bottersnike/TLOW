private static List<int> function(int a, int b){
    List<int> output = new List<int>(); int factors = 0;
    for (int i = a; i < b; i++){
        int current = 0;
        for (int j = 1; j <= i; j++) if (i % j == 0) current++;
        if (current > factors){ output = new List<int>(); factors = current; }
        if (current >= factors) output.Add(i); 
    }
    return output;
}
