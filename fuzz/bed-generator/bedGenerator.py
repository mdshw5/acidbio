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
    def line(self, parent=None):
        current = UnparserRule(name='line', parent=parent)
        self.enter_rule(current)
        self.chrom(parent=current)
        UnlexerRule(src='\t', parent=current) 
        self.coordinate(parent=current)        
        self.exit_rule(current)
        return current
    line.min_depth = 2

    @depthcontrol
    def chrom(self, parent=None):
        current = UnparserRule(name='chrom', parent=parent)
        self.enter_rule(current)
        choice = self.model.choice(current, 0, [0 if [1, 1][i] > self.max_depth else w for i, w in enumerate([1, 1])])
        if choice == 0:
            if self.max_depth >= 0:
                for _ in self.model.quantify(current, 0, min=1, max=inf):
                    self.CHAR(parent=current)
        elif choice == 1:
            self.chromName(parent=current)        
        self.exit_rule(current)
        return current
    chrom.min_depth = 1

    @depthcontrol
    def coordinate(self, parent=None):
        current = UnparserRule(name='coordinate', parent=parent)
        self.enter_rule(current)
        self.NUM(parent=current)        
        self.NUM(parent=current)        
        self.NUM(parent=current)        
        self.NUM(parent=current)        
        self.NUM(parent=current)        
        self.NUM(parent=current)        
        UnlexerRule(src='\t', parent=current)        
        self.NUM(parent=current)        
        self.NUM(parent=current)        
        self.NUM(parent=current)        
        self.NUM(parent=current)        
        self.NUM(parent=current)        
        self.NUM(parent=current)        
        self.exit_rule(current)
        return current
    coordinate.min_depth = 1

    @depthcontrol
    def chromName(self, parent=None):
        current = UnparserRule(name='chromName', parent=parent)
        self.enter_rule(current)
        UnlexerRule(src='chr', parent=current)        
        choice = self.model.choice(current, 0, [0 if [1, 0, 0, 0][i] > self.max_depth else w for i, w in enumerate([1, 1, 1, 1])])
        if choice == 0:
            choice = self.model.choice(current, 1, [0 if [1, 1, 1][i] > self.max_depth else w for i, w in enumerate([1, 1, 1])])
            if choice == 0:
                self.NUM(parent=current)
            elif choice == 1:
                UnlexerRule(src='1', parent=current)
                self.NUM(parent=current)
            elif choice == 2:
                UnlexerRule(src='2', parent=current)
                self.NUM3(parent=current)
        elif choice == 1:
            UnlexerRule(src='X', parent=current)
        elif choice == 2:
            UnlexerRule(src='Y', parent=current)
        elif choice == 3:
            UnlexerRule(src='M', parent=current)        
        self.exit_rule(current)
        return current
    chromName.min_depth = 0

    @depthcontrol
    def CHAR(self, parent=None):
        current = UnlexerRule(name='CHAR', parent=parent)
        self.enter_rule(current)
        choice = self.model.choice(current, 0, [0 if [0, 0, 0, 1][i] > self.max_depth else w for i, w in enumerate([1, 1, 1, 1])])
        if choice == 0:
            UnlexerRule(src=self.char_from_list(range(97, 123)), parent=current)
        elif choice == 1:
            UnlexerRule(src=self.char_from_list(range(65, 91)), parent=current)
        elif choice == 2:
            UnlexerRule(src='_', parent=current)
        elif choice == 3:
            self.NUM(parent=current)        
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

    @depthcontrol
    def NUM3(self, parent=None):
        current = UnlexerRule(name='NUM3', parent=parent)
        self.enter_rule(current)
        UnlexerRule(src=self.char_from_list(range(48, 52)), parent=current)        
        self.exit_rule(current)
        return current
    NUM3.min_depth = 0

    default_rule = line
