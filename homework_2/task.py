from abc import ABCMeta, abstractmethod

# 1st level in hierarchy

class ProgrammingLanguage(metaclass=ABCMeta):
    def __init__(self, name, release_year):
        self._name = name
        self._release_year = release_year

    def __str__(self):
        return self._name + ' ' + self._release_year
    
    @abstractmethod
    def run(self):
        '''
        Should run particular language code
        '''


# 2nd level in hierarchy

class ImperativeLanguage(ProgrammingLanguage):
    def __init__(self, name, release_year):
        super().__init__(name, release_year)

    def __str__(self):
        return super().__str__()
    
    def run(self):
        print('Running IMPERATIVE language code')


class DecalarativeLanguage(ProgrammingLanguage):
    def __init__(self, name, release_year):
        super().__init__(name, release_year)

    def __str__(self):
        return super().__str__()
    
    def run(self):
        print('Running DECLARATIVE language code')

# 3rd level in hierarchy


class OOP_Language(ImperativeLanguage):
    def __init__(self, name, release_year, multiple_inheritance):
        self._multiple_inheritance = multiple_inheritance
        super().__init__(name, release_year)

    def __str__(self):
        return super().__str__() + '\n' + \
               f'Multiple inheritance: {self._multiple_inheritance}'
    
    def run(self):
        print('Running OOP language code')


class FunctionalLanguage(DecalarativeLanguage):
    def __init__(self, name, release_year):
        super().__init__(name, release_year)

    def __str__(self):
        return super().__str__()
    
    def run(self):
        print('Running FUNCTIONAL language code')


# 4th level in hierarchy

class MultiParadigmLanguageFactory:
    '''
    A metaclass whose instances are classes 
    that inherit given list of classes
    '''
    def __new__(meta_cls, *instance_args, cls_name, cls_bases, ):
        cls = type(cls_name, cls_bases, {}) # creating class with given name and bases
        instance = super().__new__(cls)     # then creating its instance 
        instance.__init__(*instance_args)   # and initializing that instance
        return instance


def start():
    java = OOP_Language('Java', '1996', 'not supported')
    print(java)
    java.run()
    print('\n\n')

    sql = DecalarativeLanguage('SQL', '1986')
    print(sql)
    sql.run()
    print('\n\n')


    py = MultiParadigmLanguageFactory('Python', '1991', 'supported',
                                      cls_name='MultiParagimLanguage', 
                                      cls_bases=(OOP_Language, FunctionalLanguage))
    print(py)
    py.run() # will print OOP because it's located before Functional in mro order of py.__clas__ 
    print(f'Class: {py.__class__}')
    print(f'Base classes: {py.__class__.__bases__}')


if __name__ == '__main__':
    start()