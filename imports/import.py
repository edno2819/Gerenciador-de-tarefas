import tablib
from import_export import resources
from tarefas.models import *


book_resource = resources.modelresource_factory(model=Soda)()
dataset = tablib.Dataset(['', 'Brassagem 1', 'Teste de Nova tarefa', '2', '10/05/2022', 1, '', '' ], 
                         headers=['id', 'area', 'nome', 'responsavel', 'prazo', 'situacao', 'created_at', 'updated_at']
                         )
result = book_resource.import_data(dataset, dry_run=True)

print(result.has_errors())

result = book_resource.import_data(dataset, dry_run=False)