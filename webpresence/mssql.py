import pymssql

class Mssql:
    """
    This class is supposed to do dirty work. A lot of hardcoded SQL and parameters etc.
    """

    def __init__(self, host,user,password,database):

        self.alunos = [] 

        conn = pymssql.connect(host, user, password, database)
        self.cursor = conn.cursor(as_dict=True)

    def todos_alunos(self):
        """
        Return all the students (and only students).

        Returns:
            (dict): All the students.
        """

        self.cursor.execute('select codigo,codext,nome from "sophia"."FISICA" where codext is not null; select codigo,codext,nome from "sophia"."FISICa" where codext is not null')

        query_alunos = self.cursor.fetchall()

        return query_alunos

    def dadospf(self, codigo_aluno):
        """
        Return the relation between students and family.

        Args:
            codigo_aluno(int): The student's primary key.

        Returns:
            (dict): Two data (the primary key itself and the family foreign key).
        """

        self.cursor.execute('select fisica,familia from "sophia"."DADOSPF" where fisica=' + str(codigo_aluno))

        query_dadospf = self.cursor.fetchall()

        return query_dadospf

    def dados_familia(self, codigo_familia):
        """
        Return the family data. In other words: parents data (email, identification document and name).

        Args:
            codigo_familia(int): The primary key from the family table.

        Returns:
            (dict): All the student's parents data.
        """

        self.cursor.execute('select codigo,pai_nome,pai_email,pai_cpf, mae_nome,mae_email,mae_cpf from "sophia"."FAMILIAS" where codigo=' + str(codigo_familia))

        query_familia = self.cursor.fetchall()

        return query_familia

    def gera_dados_alunos(self):
        """
        Populate the list of students filling it with student's data.

        Returns:
            (dict): All student's data.
        """

        apenas_alunos = self.todos_alunos()

        for dados in apenas_alunos:

            dados_aluno = {}

            dados_aluno['codigo'] = dados['codigo']
            dados_aluno['matricula'] = dados['codext'].encode('utf-8')
            dados_aluno['nome'] = dados['nome'].encode('utf-8')

            query_dadospf = self.dadospf(codigo_aluno=str(dados_aluno['codigo']))

            for dados_pf in query_dadospf:
                dados_aluno['codigo_familia'] = dados_pf['familia']

            if not dados_aluno['codigo_familia']:
                dados_aluno['codigo_familia'] = 0
                dados_aluno['pai_nome'] = 'None'  
                dados_aluno['pai_email'] = 'None' 
                dados_aluno['pai_cpf'] = 'None' 
                dados_aluno['pai_cpf'] = 'None' 
                dados_aluno['mae_nome'] = 'None' 
                dados_aluno['mae_email'] = 'None' 
                dados_aluno['mae_cpf'] = 'None' 
                dados_aluno['mae_cpf'] = 'None' 

            query_familia = self.dados_familia(dados_aluno['codigo_familia'])

            for dados_familia in query_familia:
                dados_aluno['pai_nome'] = dados_familia['pai_nome']
                dados_aluno['pai_email'] = dados_familia['pai_email']
                dados_aluno['pai_cpf'] = str(dados_familia['pai_cpf']).replace('.','')
                dados_aluno['pai_cpf'] = str(dados_aluno['pai_cpf']).replace('-','') 
                dados_aluno['mae_nome'] = dados_familia['mae_nome']
                dados_aluno['mae_email'] = dados_familia['mae_email']
                dados_aluno['mae_cpf'] = str(dados_familia['mae_cpf']).replace('.','')
                dados_aluno['mae_cpf'] = str(dados_aluno['mae_cpf']).replace('-','') 

            self.alunos.append(dados_aluno)

        return self.alunos
