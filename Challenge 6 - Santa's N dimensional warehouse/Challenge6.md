# Description

Welcome to Santa's Warehouse! Careful with the dimensional doors. They all lead to various parts of the high dimensional storage space. What is it? Funny you should ask. It's where Santa keeps all of the presents the Elves make. How else would he store billions of packages?

It is your job to help him store and retrieve all the presents. Here is what you need to know:

- A present is identified with a sequence of letters. There may be more than one of the same kind as some people wanted the same thing.
- The list of perpendicular axis is given as a string. Each axis is denoted with a single letter. There is always at least one. There may be more.
- A move instruction is made up of the name of an axis and an integer denoting distance.
- If a move instruction refers to an axis that is not in the list, ignore that instruction. It must be for a different warehouse.

## Manifests

You will be given a list of manifests. There can be two kinds: storage and movement.

### Storage manifests

A storage manifest will have the following format:

- The presents to be stored and where to store them are separated by a colon `:`.
- The list of presents will have a positive number followed by the identifier of the present. The number denotes how many of the presents you are storing.
- The presents section may contain multiple kinds of presents that you are storing at once.
- The location section will have a sequence of movement instructions which lead to where the present is stored. You are moving the presents from the origin of the axis (where the main entrance is).

### Movement manifests

A movement manifest will have the following format:

- The first part indicates which presents to move, the second is how to move them. These are separated by a colon `:`.
- The location is given as a set of movement instructions from the origin.
- Then the presents are moved from their current location by the movements specified in the second set of instructions.

Santa doesn't like to look for the same present in multiple places. So if you are storing a present that is already in the warehouse, instead of following the placement instructions you should put it where the same kind of present is already stored.

## Intructions

You are given a string denoting the cardinal axis of the warehouse. You are given a list of manifests. You are also given a location that Santa wants to check as a sequence of movement instructions from the origin. Return the contents of that location as a single string. It should be ordered first by the number of presents (ascending) then alphabetically by the identifier of the present.

## Example

Let's consider a simple example. In this case it's only a 2-dimensional warehouse, where the axis are named `X` and `Y` so the list of axis is `"XY"`. You are given the following manifests.

`"3A:X10", "X10:X10Y-5", "4C:X20Y-10Y5"`

- The first instruction tells you to move $3$ `A` presents from the origin $10$ along the `X` axis.
- The second instruction tells you to move all presents from `X10` and move them $10$ along the `X` axis and $-5$ along the `Y` which will end up at `X20Y-5`.
- The third instruction tells you to move $4$ `C` presents from the origin $20$ along the `X`, $-10$ along the `Y` axis and then $5$ along the `Y` axis. They will also end up at `X20Y-5`.

Finally, you are asked to get all the presents from `Y-5X20` which is where all the presents are stored currently. You would return `3A4C` which are all the presents, sorted correctly.

Best of luck! Christmas depends on you.