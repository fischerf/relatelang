define Prisoner as "Ein Gefangener, der seine Nummer sucht".
define Box as "Eine Schachtel, die eine Nummer enthält".
define Game as "Das Gesamtspiel mit allen Regeln".
define Strategy as "Die Strategie der Gefangenen".

Prisoner has number of 0.
Prisoner has attempts_left of 50.
Prisoner has found_number of false.
Box has contains_number of 0.
Box has is_opened of false.
Game has total_prisoners of 100.
Game has success_rate of 0.
Strategy has is_loop_following of true.

Game is active.
Game is not completed.
Strategy is optimal.
Box is available.

relate Prisoner and Box as "checks" if Box is available and Prisoner has attempts_left of >0.
relate Box and Prisoner as "contains_number_of" if Box has contains_number of Prisoner has number.
relate Strategy and Prisoner as "guides" if Strategy is optimal.

if Prisoner checks Box and Box contains_number_of Prisoner, then ensure Prisoner has found_number of true.
if Prisoner has attempts_left of 0 and Prisoner has found_number of false, then ensure Game is completed.
if Prisoner has found_number of true, then ensure Game has success_rate of +1.

if Strategy is loop_following, then ensure Prisoner checks Box with contains_number of Prisoner has number.

ensure all Prisoner has found_number of true.
ensure Game has success_rate of >30.