import chapter1problems

if __name__ == "__main__":
    # tests for problem 1.1
    assert chapter1problems.isunique("token") is True, "String token failed isUnique test."
    assert chapter1problems.isunique("babe") is False, "String babe failed isUnique test."
    assert chapter1problems.isunique("") is True, "Empty string failed isUnique test."
    assert chapter1problems.isunique("...") is False, "String ... failed isUnique test."

    assert chapter1problems.isuniqueinplace("token") is True, "String token failed isUniqueInPlace test."
    assert chapter1problems.isuniqueinplace("babe") is False, "String babe failed isUniqueInPlace test."
    assert chapter1problems.isuniqueinplace("") is True, "Empty string failed isUniqueInPlace test."
    assert chapter1problems.isuniqueinplace("...") is False, "String ... failed isUniqueInPlace test."
    print("Problem 1.1 tests complete.")

    # tests for problem 1.2
    assert chapter1problems.ispermutation("toga", "goat") is True, "Permutation test failed for inputs: toga and goat."
    assert chapter1problems.ispermutation("boat", "bat") is False, "Permutation test failed for inputs: boat and bat."
    assert chapter1problems.ispermutation("a gasp", "as pag") is True, "Permutation test failed for inputs: a gasp and as pag."
    assert chapter1problems.ispermutation("who.", ".how") is True, "Permutation test failed for inputs: who. and .how "
    assert chapter1problems.ispermutation("Faith", "faith") is True, "Permutation test failed for inputs: Faith and faith."
    assert chapter1problems.ispermutation("", "") is True, "Permutation test failed for inputs: empty strings."
    print("Problem 1.2 tests complete.")

    # tests for problem 1.3
    assert chapter1problems.urlifyinplace(["a"," ","b"," ","c"," "," "," "," "], 5) == "a%20b%20c", "Urlify on 'a b c    ' has failed."

    print("Problem 1.3 tests complete.")



