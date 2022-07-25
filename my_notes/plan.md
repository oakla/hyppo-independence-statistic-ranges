1. Simulate data
    - simulate a single data sets (specific distros)
    - store each in list of tuples (type, data, parameters)
      - [ ] zeros
      - [ ] ones
      - [ ] ints
      - [ ] floats
      - [ ] normal
      - [ ] poisson
      - [ ] logistic
    - simulate a single data sets (other distros)
      - [ ] ?
    - simulate correlated data
      - [ ] setup converter for a given map
      - [ ] do the same for other maps
      - [ ] store each pair in a list
    - simulate uncorrelated data
      - use above list to create table of randomised pairs where pairings:
        1. do not repeat, and 
        2. do not mimic original pairs

2. Run a trial an firgure out how to store data
   - things to store
     - `(pvalue, stat)` as per `test()` method
     - `stat` as per `statistic` method
     - dataset 1 shape
     - dataset 2 shape
     - distribution parameters and type
3. 
4. Run trials
   - run test for each dependent pair
   - run test for random independent pairs