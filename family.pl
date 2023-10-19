female(pam).%clauses
female(liz).
female(pat).
female(ann).

male(jim).
male(bob).
male(tom).
male(peter).

parent(pam,bob).
parent(tom,bob).
parent(tom,liz).
parent(bob,ann).
parent(bob,pat).
parent(pat,jinm).
parent(bob,peter).
parent(peter,jim).

mother(X,Y):-parent(X,Y),female(x).
father(X,Y):-parent(X,Y),male(X).
sister(X,Y):-parent(X,Z),parent(Y,Z),female(X).
brother(X,Y):-parent(X,Z),parent(Y,Z),male(X).
