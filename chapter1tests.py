import chapter1problems

if __name__ == "__main__":
    ############ tests for problem 1.1 ####################################################
    assert chapter1problems.isunique("token") is True, "String token failed isUnique test."
    assert chapter1problems.isunique("babe") is False, "String babe failed isUnique test."
    assert chapter1problems.isunique("") is True, "Empty string failed isUnique test."
    assert chapter1problems.isunique("...") is False, "String ... failed isUnique test."

    assert chapter1problems.isuniqueinplace("token") is True, "String token failed isUniqueInPlace test."
    assert chapter1problems.isuniqueinplace("babe") is False, "String babe failed isUniqueInPlace test."
    assert chapter1problems.isuniqueinplace("") is True, "Empty string failed isUniqueInPlace test."
    assert chapter1problems.isuniqueinplace("...") is False, "String ... failed isUniqueInPlace test."
    print("Problem 1.1 tests complete.")

    ############## tests for problem 1.2 ########################################################
    assert chapter1problems.ispermutation("toga", "goat") is True, "Permutation test failed for inputs: toga and goat."
    assert chapter1problems.ispermutation("boat", "bat") is False, "Permutation test failed for inputs: boat and bat."
    assert chapter1problems.ispermutation("a gasp", "as pag") is True, "Permutation test failed for inputs: a gasp " \
                                                                       "and as pag."
    assert chapter1problems.ispermutation("who.", ".how") is True, "Permutation test failed for inputs: who. and .how "
    assert chapter1problems.ispermutation("Faith", "faith") is True, "Permutation test failed for inputs: Faith and " \
                                                                     "faith."
    assert chapter1problems.ispermutation("", "") is True, "Permutation test failed for inputs: empty strings."
    print("Problem 1.2 tests complete.")

    ############# tests for problem 1.3 ###########################################################
    assert chapter1problems.urlifyinplace(["a", " ", "b", " ", "c", " ", " ", " ", " "], 5) == ['a', '%', '2', '0', 'b',
                                                                                                '%', '2', '0',
                                                                                                'c'], \
        "Urlify on 'a b c    ' has failed."
    assert chapter1problems.urlifyinplace(
        ["m", "r", " ", "j", "o", "h", "n", " ", "s", "m", "i", "t", "h", " ", " ", " ", " "], 13) == ['m', 'r', '%',
                                                                                                       '2', '0',
                                                                                                       'j', 'o', 'h',
                                                                                                       'n', '%', '2',
                                                                                                       '0', 's', 'm',
                                                                                                       'i', 't', 'h'],\
        "Urlify on 'mr john smith' has failed."
    assert chapter1problems.urlifyinplace(['a', 'c', 'd', 'c'], 4) == ['a', 'c', 'd', 'c'], \
        "Urlify on acdc has failed."
    assert chapter1problems.urlifyinplace([' ', ' ', ' ', ' '], 1) == ['%', '2', '0', ' '], \
        "Urlify on all spaces has failed."

    print("Problem 1.3 tests complete.")

    ################# tests for problem 1.4 ###########################################################
    assert chapter1problems.permpalindrome("tacocat") is True, "Permpalindrome failed for tacocat."
    assert chapter1problems.permpalindrome("taco cat") is True, "Permpalindrome failed for taco cat."
    assert chapter1problems.permpalindrome("act o cat") is True, "Permpalindrome failed for act o cat."

    assert chapter1problems.permpalindrome("taco ca") is False, "Permpalindrome failed for taco ca."
    assert chapter1problems.permpalindrome("ababc") is True, "Permpalindrome failed for ababc."
    assert chapter1problems.permpalindrome(" ") is True, "Permpalindrome failed for blank space."
    assert chapter1problems.permpalindrome("abcde") is False, "Permpalindrome failed for abcde."



    ############### tests for 1.4 with bit manipulation ##################################
    assert chapter1problems.ispalindromepermutation("tacocat") is True, "Ispalindromepermutation failed for tacocat."
    assert chapter1problems.ispalindromepermutation("taco cat") is True, "Ispalindromepermutation failed for taco cat."
    assert chapter1problems.ispalindromepermutation("act.o cat") is True, "Ispalindromepermutation failed for " \
                                                                          "act.o cat."

    assert chapter1problems.ispalindromepermutation("taco ca") is False, "Ispalindromepermutation failed for taco ca."
    assert chapter1problems.ispalindromepermutation("ababc") is True, "Ispalindromepermutation failed for ababc."
    assert chapter1problems.ispalindromepermutation(" ") is True, "Ispalindromepermutation failed for blank space."
    assert chapter1problems.ispalindromepermutation("abcde") is False, "Ispalindromepermutation failed for abcde."

    print("Problem 1.4 tests complete.")

    ############## tests for problem 1.5 ####################################################
    assert chapter1problems.oneaway("bob", "bob") is True, "One away has failed for 'bob','bob'."
    assert chapter1problems.oneaway("boat", "bot") is True, "One away has failed for 'boat','bot'."
    assert chapter1problems.oneaway("boar", "bot") is False, "One away has failed for 'boar','bot'."
    assert chapter1problems.oneaway("bow", "bot") is True, "One away has failed for 'bow','bot'."
    assert chapter1problems.oneaway("", "") is True, "One away has failed for two empty strings."

    print("Problem 1.5 tests complete.")

    ############# tests for problem 1.6 ######################################################
    assert chapter1problems.compresstring("aaabbbccdddd") == "a3b3c2d4", "Compress String failed for 'a3b3c2d4'."
    assert chapter1problems.compresstring("aabbccd") == "aabbccd", "Compress String failed for 'aabbccd'."
    assert chapter1problems.compresstring("abbbcbbbdbbb") == "a1b3c1b3d1b3", "Compress String failed for " \
                                                                             "'abbbcbbbdbbb'."
    print("Problem 1.6 tests complete.")



