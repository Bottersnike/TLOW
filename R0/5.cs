kstatic string r0(string input){

    string output = ""; int max = 0;

    for (int shift = 0; shift < 26; shift++){

        int score = 0; string str = "", good = "aeioustrhnl", bad = "zxwvqjk";

        foreach (char letter in input){
            str += (letter == ' ') ? ' ' : (char)((letter + shift - 'a') % 26 + 'a');
            if (good.Contains(str[str.Length - 1] + "")) score += 1;
            if (bad.Contains(str[str.Length - 1] + "")) score -= 2; }

        if (score > max){max = score; output = str;}

    } return output; }
