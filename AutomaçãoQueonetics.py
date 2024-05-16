import requests
from requests.auth import HTTPBasicAuth

# Base URL da API da Queonectics
base_url = "http://desafio-api-trix.trixlog.com"

# Função para criar uma organization
def criar_organization(name, parent_org_id, description, level_id, username, password):
    url = f"{base_url}/organization"

    payload = {
        "parentOrganization": {
            "id": parent_org_id
        },
        "name": name,
        "description": description,
        "hierarchicalLevel": {
            "id": level_id,
            "name": "Regioes do Brasil",
            "description": "Nivel 2",
            "level": 2,
            "isLevelDetailed": True
        }
    }

    response = requests.post(url, json=payload)

    auth = HTTPBasicAuth(username, password)

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, auth=auth, headers=headers)

    # Verifica o status da resposta
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro na requisição HTTP: {response.status_code}")
        return None
    

# Função para criar um driverTeam
def criar_driver_team(team_name, team_description, organization_id, representatives, username, password):
    url = f"{base_url}/driverteam"

    payload = {
        "drivers": [
        ],
        "name": team_name,
        "description": team_description,
        "organization": {
            "id": organization_id
        },
        "secundaryOrganizations": [],
        "filiationType": "INHERENT",
        "representatives": representatives
    }

    auth = HTTPBasicAuth(username, password)

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, auth=auth, headers=headers)

    # Verifica o status da resposta
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro na requisição HTTP: {response.status_code}")
        return None

# Função para criar um driver
def criar_driver(license_category_two, name, type_driver, registration, team_id, status, hiringType, birth_date, identificationType, license_qtd, licenseRegister, license_category, licenseExpedition, licenseExpiration, username, password):
    url = f"{base_url}/driver"

    payload = {
        "name": name,
        "type": type_driver,
        "registration": registration,
        "driverTeam": {
            "id": team_id
        },
        "status": status,
        "hiringType": hiringType,
        "identificationType": identificationType,
        "birthDate": birth_date,
        "firstLicense": birth_date,
        "license": license_qtd,
        "licenseRegister": licenseRegister,
        "licenseCategory": [license_category],
        "licenseExpedition": licenseExpedition,
        "licenseExpiration": licenseExpiration,
        "identifications": [],
        "licenses": [
            {
                "license": license_category_two
            }
        ]
    }

    auth = HTTPBasicAuth(username, password)

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, auth=auth, headers=headers)

    # Verifica o status da resposta
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro na requisição HTTP: {response.status_code}")
        return None


def criar_driver(payload, username, password):
    url = f"{base_url}/driver"


    auth = HTTPBasicAuth(username, password)

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, auth=auth, headers=headers)

    # Verifica o status da resposta
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro na requisição HTTP: {response.status_code}")
        return None

# Função para criar um group
def criar_group(organization_id, disabled, name, username, password):
    url = f"{base_url}/group"
    
    payload = {
        "organization": {
            "id": organization_id
        },
        "name": name,
        "disabled": disabled
    }
    
    auth = HTTPBasicAuth(username, password)

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, auth=auth, headers=headers)

    # Verifica o status da resposta
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro na requisição HTTP: {response.status_code}")
        return None

# Teste automático dos passos
if __name__ == "__main__":

    api_username = ""
    api_password = ""

    # Criar uma organization (deve ser filha de outra organização, vamos usar parent_id=2)
    # ID da organização pai (exemplo: 2)
    parent_organization_id = 2

    # Informações da nova organização conforme o payload fornecido
    nome_nova_org = "Organização pai 2 teste 9027"
    descricao_nova_org = "teste nova organização"
    level_id_nova_org = 3  # ID do nível hierárquico (exemplo: 3)
    nova_org = criar_organization(nome_nova_org, parent_organization_id, descricao_nova_org, level_id_nova_org, api_username, api_password)
    organization_id = nova_org["id"] #ID Organization criada: 924

    #para teste
    #organization_id = 924 #ID Organization criada: 924

    print("ID Organization criada: {}".format(organization_id))

    # Criar um driverTeam na organization criada anteriormente
    team_name = "Teste nome unico team teste 5"
    team_description = "Time x teste descrição"
    representatives = [442]  
    novo_driver_team = criar_driver_team(team_name, team_description, organization_id, representatives, api_username, api_password)
    driver_team_id = novo_driver_team["id"] #717

    #driver_team_id = 717

    print("ID Driver Team foi criado: {}".format(driver_team_id))

    # Criar um driver no driverTeam criado anteriormente

    name="Nome teste driver 2024 26"
    type_driver="DRIVER"
    registration="912932923934898909898012"
    status="ACTIVE"
    hiringType="TEMPORARY"
    identificationType="NONE"
    birth_date="2024-04-01T03:00:00.000Z"
    firstLicense="2024-04-05T03:00:00.000Z"
    license_qtd="1"
    licenseRegister="1"
    license_category="[A]"
    licenseExpedition="2024-05-01T00:00:00.000Z"
    licenseExpiration="2024-05-22T00:00:00.000Z"
    license_category_in_licenses = "A"


    payload_criar_driver = {
        "name": name,
        "type": type_driver,
        "registration":  registration,
        "driverTeam": {
            "id": driver_team_id
            },
        "status": status,
        "hiringType": hiringType,
        "identificationType": identificationType,
        "birthDate":  birth_date,
        "firstLicense": firstLicense,
        "license": license_qtd,
        "licenseRegister": licenseRegister,
        "licenseCategory": license_category,
        "licenseExpedition": licenseExpedition,
        "licenseExpiration": licenseExpiration,
        "identifications": [],
        "licenses": [
            {
                "license": license_category_in_licenses
            }
        ]
    }

    novo_driver = criar_driver(payload_criar_driver, api_username, api_password)
    id_novo_driver = novo_driver["id"]
    print("Novo Driver: {}".format(id_novo_driver))

    # Criar um group na organization criada
    group_name = "novo nome grupo 2024 novo 3"
    disabled = False

    novo_group = criar_group(organization_id, disabled, group_name, api_username, api_password)
    id_novo_grupo = novo_group["id"]
    print("Novo Group: {}".format(id_novo_grupo))

    print("Entidades criadas com sucesso!")
