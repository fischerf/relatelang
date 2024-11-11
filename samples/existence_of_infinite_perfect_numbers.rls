define Number as "A natural number greater than 1".
Number has value of n.
Number has type of "natural".

define Divisor as "A natural number that divides another number without remainder".
Divisor has value of d.
Divisor has type of "natural".

define ProperDivisor as "A divisor of a number that is less than the number itself".
ProperDivisor is Divisor.
ProperDivisor has value less than Number.

define DivisorSum as "The sum of all proper divisors of a number".
DivisorSum has value of s.
DivisorSum has type of "natural".

relate Divisor and Number as "divides" if 
    Number mod Divisor equals 0.

relate ProperDivisor and Number as "proper_divides" if
    ProperDivisor divides Number and
    ProperDivisor is less than Number.

relate DivisorSum and Number as "sums_to" if
    DivisorSum equals sum of all ProperDivisor where
    ProperDivisor proper_divides Number.

define PerfectNumber as "A number that equals the sum of its proper divisors".
PerfectNumber is Number.
PerfectNumber has property "perfect".

relate Number and PerfectNumber as "is_perfect" if
    Number equals DivisorSum where
    DivisorSum sums_to Number.

define InfinitePerfectNumber as "A perfect number that is infinite".
InfinitePerfectNumber is PerfectNumber.
InfinitePerfectNumber has size of "infinite".

# The mathematical problem
ensure exists InfinitePerfectNumber.

# Known constraints
relate PerfectNumber and Number as "is_even" if
    PerfectNumber mod 2 equals 0.

# Euclid-Euler theorem
define EuclidForm as "2^(p-1) * (2^p - 1) where p is prime and 2^p - 1 is prime".
relate PerfectNumber and EuclidForm as "follows_form" if
    PerfectNumber is even.

# The open question
ensure exists InfinitePerfectNumber where
    InfinitePerfectNumber is not even.

# Historical context
define OddPerfectNumber as "A perfect number that is odd".
OddPerfectNumber is PerfectNumber.
OddPerfectNumber has property "odd".

ensure not proven exists OddPerfectNumber.
ensure not proven not exists OddPerfectNumber.