% FAMILY TREE PROGRAM

% Male 
male(john).
male(peter).
male(mark).
male(sam).
male(david).

% Female 
female(mary).
female(linda).
female(susan).
female(anna).
female(kate).

% Parent relationships
parent(john, peter).
parent(mary, peter).

parent(john, linda).
parent(mary, linda).

parent(peter, sam).
parent(susan, sam).

parent(peter, anna).
parent(susan, anna).

parent(linda, david).
parent(mark, david).

parent(linda, kate).
parent(mark, kate).

% ---------- Rules ----------

% Father
father(X, Y) :-
    male(X),
    parent(X, Y).

% Mother
mother(X, Y) :-
    female(X),
    parent(X, Y).

% Child
child(X, Y) :-
    parent(Y, X).

% Grandparent
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% Grandchild
grandchild(X, Y) :-
    grandparent(Y, X).

% Siblings
sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

% Cousins
cousin(X, Y) :-
    parent(A, X),
    parent(B, Y),
    sibling(A, B).

% Uncle
uncle(X, Y) :-
    male(X),
    sibling(X, Z),
    parent(Z, Y).

% Aunt
aunt(X, Y) :-
    female(X),
    sibling(X, Z),
    parent(Z, Y).