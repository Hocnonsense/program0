class Genome(object):
    _root = list()
    def __init__(self, treeNumber):
        self.__treeNumber = treeNumber*2+1
        self.__version = 0
        Genome._root.append(self)
        if treeNumber > 0x7FFF:  # 则 self.__treeNumber 超过0x10000. 否则属于 15 代以内, 共用一棵树. 
            self().Reset()

    def __getTreeNumber(self):
        return self.__treeNumber
    treeNumber = property(fget = __getTreeNumber)

    @classmethod
    def Reset(cls, genome, filename = ""):
        print("命名二叉树到达极限, 但是暂时还没写好如何重置")
        input()

class Vector(Genome):
    def __init__(self, treeNumber, genes, c):
        super().__init__(self, treeNumber)
        self.__genes = genes

    def commend(self):
        """
            在这里接受命令, 并返回相应特征值
        """
        proteins = list()
        return proteins
