class ExpLink:
    def __init__(self, val, exp, next=None):
        self.val = val
        self.exp = exp
        self.next = next

class PolyAdd:
    def add(p, q):

        # z starts out as 0 * biggest degree + 1
        z = ExpLink(0, max(p.exp, q.exp) + 1)
        t = z

        # iterate through both linked lists
        # add coefficients together on case by case basis
        while p != None or q != None:
                
            # if p or q is None
            if not p:
                t.next = ExpLink(q.val, q.exp)
                q, t = q.next, t.next
                continue
            elif not q:
                t.next = ExpLink(p.val, p.exp)
                p, t = p.next, t.next
                continue

            # exponents are the same (only add if nonzero)
            if p.exp == q.exp and p.val + q.val != 0:
                t.next = ExpLink(p.val + q.val, p.exp)
                p, q, t = p.next, q.next, t.next

            # p's exponent is less than q's exponent
            # just add p's node to the result and move on
            elif p.exp < q.exp:
                t.next = ExpLink(p.val, p.exp)
                p, t = p.next, t.next
                
            # q's exponent is less than q's exponent
            # just add q's node to the result and move on
            elif q.exp < p.exp:
                t.next = ExpLink(q.val, q.exp)
                q, t = q.next, t.next
            
        return z.next

# p = ExpLink(2, 0, ExpLink(3, 2, ExpLink(2, 4)))
# q = ExpLink(3, 2, ExpLink(1, 3))
# r = PolyAdd.add(p, q)