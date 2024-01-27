# ecoinv
first commit

pip install -r requirements.txt
docker pull postgres
docker run --name EcoInventDB -e POSTGRES_PASSWORD=TheBestPassword -e POSTGRES_USER=admin -e POSTGRES_DB=database -p 5432:5432 -d postgres
4822a70c59308f355bc9bcf8acf224e43d39b10586475a9a1658846109e921ff

