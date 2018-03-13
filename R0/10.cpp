string decoder(string str)
{
    int vals[26] = {110,20,38,57,172,30,27,82,94,2,10,54,33,91,101,26,1,81,86,122,37,13,32,2,27,1};
    int s[26] = {}, num[26] = {}, le = str.length(), t; char lett[le]; strcpy(lett, str.c_str());
    for (int i = 0; i < le; i++) if  (lett[i] != 32) num[lett[i] - 97] = num[lett[i] - 97] + 1;
    for (int i = 0; i < 26; i++) for (int j = 0; j < 26; j++) s[i] += num[j] * vals[(j + i) % 26];
    for (int i = 0; i < 26; i++) for (int j = 0; j < 2; j++) t = distance(s, max_element(s, s + 26));
    for (int i = 0; i < le; i++) if  (lett[i] != 32) lett[i] = (lett[i] - 97 + t) % 26 + 97; str = lett;
    return str;
}
