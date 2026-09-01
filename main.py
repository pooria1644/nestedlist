class nestedlist(list):
    def __getitem__(self, i: int|slice|tuple[int, ...]):
        try:
            res = self
            for j in i:
                res = res[j]
            return res
        except:
            return list(self).__getitem__(i)


nl = nestedlist
