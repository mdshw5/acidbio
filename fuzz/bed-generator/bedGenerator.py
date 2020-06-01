# Generated by Grammarinator 19.3+46.gbc14ea2

from itertools import chain
from math import inf
from grammarinator.runtime import *


class bedGenerator(Generator):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def EOF(self, *args, **kwargs):
        pass


    @depthcontrol
    def chrom(self, parent=None):
        current = UnparserRule(name='chrom', parent=parent)
        self.enter_rule(current)
        choice = self.model.choice(current, 0, [0 if [1, 2][i] > self.max_depth else w for i, w in enumerate([1, 1])])
        if choice == 0:
            if self.max_depth >= 0:
                for _ in self.model.quantify(current, 0, min=1, max=inf):
                    self.CHAR(parent=current)
        elif choice == 1:
            UnlexerRule(src='chr', parent=current)
            self.NUMBER(parent=current)        
        self.exit_rule(current)
        return current
    chrom.min_depth = 1

    @depthcontrol
    def CHAR(self, parent=None):
        current = UnlexerRule(name='CHAR', parent=parent)
        self.enter_rule(current)
        choice = self.model.choice(current, 0, [0 if [0, 0, 0, 0][i] > self.max_depth else w for i, w in enumerate([1, 1, 1, 1])])
        if choice == 0:
            UnlexerRule(src=self.char_from_list(range(97, 123)), parent=current)
        elif choice == 1:
            UnlexerRule(src=self.char_from_list(range(65, 91)), parent=current)
        elif choice == 2:
            UnlexerRule(src='_', parent=current)
        elif choice == 3:
            UnlexerRule(src=self.char_from_list(range(48, 58)), parent=current)        
        self.exit_rule(current)
        return current
    CHAR.min_depth = 0

    @depthcontrol
    def NUMBER(self, parent=None):
        current = UnlexerRule(name='NUMBER', parent=parent)
        self.enter_rule(current)
        if self.max_depth >= 0:
            for _ in self.model.quantify(current, 0, min=1, max=inf):
                self.NUM(parent=current)        
        self.exit_rule(current)
        return current
    NUMBER.min_depth = 1

    @depthcontrol
    def NUM(self, parent=None):
        current = UnlexerRule(name='NUM', parent=parent)
        self.enter_rule(current)
        UnlexerRule(src=self.char_from_list(range(48, 58)), parent=current)        
        self.exit_rule(current)
        return current
    NUM.min_depth = 0

    default_rule = chrom
