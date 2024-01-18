from ocean import Ocean

class TestOcean: 
    init_state = [ 
        [0, 2, 0, 1, 3], 
        [0, 2, 0, 3, 3], 
        [0, 2, 2, 2, 1], 
        [2, 1, 2, 0, 3], 
        [3, 3, 1, 3, 3], 
    ] 
 
    next_state = [ 
        [0, 0, 0, 1, 3], 
        [2, 2, 0, 3, 3], 
        [2, 0, 0, 2, 1], 
        [0, 1, 2, 2, 3], 
        [0, 0, 1, 3, 3], 
    ] 

    def test_ocean_init(self): 
        ocean = Ocean(self.init_state)
        assert str(ocean) == "\n".join( 
            [" ".join(str(el) for el in row) for row in self.init_state] 
        ) 
 
    def test_ocean_repr(self): 
        ocean = Ocean(self.init_state)
        assert ocean.repr() == f"Ocean({self.init_state!r})" 
 
    def test_ocean_step(self): 
        ocean = Ocean(self.init_state)
        next_state = ocean.gen_next_quantum()
        assert str(next_state) == "\n".join( 
            [" ".join(str(el) for el in row) for row in self.next_state] 
        )