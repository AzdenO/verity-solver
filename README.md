# Verity Solver

Verity Salvations Edge encounter outside solver

## Introduction

This project aims to assist a player in solving the outside puzzle in verity, where shapes need to be swapped between statues to achieve a specific "escape shape" on each statue. At current, it is near optimal, there are however 2 edge cases discovered that give 3 instructions to a correct solve, but in reality should only give two.

## What is Verity?

Verity is the 4th encounter in the Salvations Edge raid in Destiny 2. It consists of 3 "inside" rooms with a player teleported to one of each room, with 3 people left on the "outside" room.

### Inside Rooms

There is 1 player to each of the 3 inside rooms. In each inside room there are 3 statues, 1 of each of the 3 players teleported to a room; a LEFT, MID and RIGHT. Each player statue is holding one of 3 2D shapes, circle, triangle or square. The aim is for each inside player to have picked up the two other shapes that their statue is NOT holding.

When teleported inside, each player can see a shadow on the back wall of their room, this shadow will morph between one and another shape after a short interval. It can morph between two different shapes, or the same shape. This shadow dictates what shapes are dropped when killing a Hive Knight. Shapes must be passed between statues/ to a different players inside so that everyone has the two shapes they need to pick up and "escape", essentially forming a 3D shape from 2 2D shapes. 

### Outside Room

The aim of the outside room is to swap shapes between 3 statues (that are of the 3 inside players but are instead holding a combination of 2 of the 3 possible 2D shapes) so that each statue is holding the correct 3D shape to allow inside players to escape. Think of it as the inside players are picking up their key, and the outside solver is forming the lock for the key. 

The only important rule is that a key cannot be formed that includes the shape that players statue is holding. So if a players statue is holding a square, they can use a triangle and a circle, a circle and a circle and a triangle and a triangle.

There are 6 possible combinations of two of the 3 2D shapes. Normally, the outside is solved by having the two opposite shapes an inside statue is holding, so holding a square, the "key/lock" is made of a triangle and a circle. However, this program also solves the "Master Challenge" which dictates that on round 2 of 3, the other 3 "perfect shapes" (i.e. CC, TT, SS and not TS, CS, TC) must be used to escape. To do this, the program assumes a "right-shift strategy" such that if the inside statues are holding C,T,S left-right, the "keys/locks" will be SS,CC,TT left-right. 