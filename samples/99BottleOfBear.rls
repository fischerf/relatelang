define Bottle as "A container of beer".
define Song as "A sequence of verses about bottles of beer".

Bottle has Number of 99.

define Verse as "A part of the song that describes taking down bottles".

ensure Song contains Verse.

if Bottle has Number of 1,
    then ensure Verse says "1 bottle of beer on the wall, 1 bottle of beer. Take one down, pass it around, no more bottles of beer on the wall."

if Bottle has Number of 2,
    then ensure Verse says "2 bottles of beer on the wall, 2 bottles of beer. Take one down, pass it around, 1 bottle of beer on the wall."

if Bottle has Number more than 2,
    then ensure Verse says "[Bottle.Number] bottles of beer on the wall, [Bottle.Number] bottles of beer. Take one down, pass it around, [Bottle.Number - 1] bottles of beer on the wall."

if Song contains Verse and Bottle has Number more than 1,
    then ensure Bottle has Number reduced by 1 and Song repeats Verse.
