# Wald-Wolfowitz
## Summary
Tests whether two samples were **indepedently** drawn from the same distribution.
- [Guide](https://hyppo.neurodata.io/user_guide/independence.html#friedman-rafsky-test-for-randomness)

- The first returned stat:
    - is the actual stat minus the mean of the null, all divided by the standard deviation of the null
    - has no set range (from `<method>.test()`)
- The second returned stat (from `<method>.statistic()`) is the *actual* test statistic


