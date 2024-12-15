import jmespath
data={
  "people": [
    {
      "name": "a",
      "state": {"name": "up"},
      "code":[{"id":84902,"number":59823},{"id":84902,"number":59823}]
    },
    {
      "name": "b",
      "state": {"name": "down"},
      "code":[{"id":84902,"number":59823},{"id":84902,"number":59823}]
    },
    {
      "name": "c",
      "state": {"name": "up"},
      "code":[{"id":84902,"number":59823},{"id":84902,"number":59823}]
    }
  ]
}
print(jmespath.search('people[*].{name:name,code:code[0]}',data))
print(jmespath.search('people[*].[name,code]',data))
print('\n')
print(jmespath.search('people[0].state',data))
print(jmespath.search('people[1].state',data))
print(jmespath.search('people[2].state',data))
print('\n')
print(jmespath.search('people[?code!=`84902`].name',data))
print(jmespath.search('people[*].state',data))
print(jmespath.search('people[*].code[*].id',data))