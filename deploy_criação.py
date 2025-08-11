project_id = '15e59289b6'
agents = client.list_agents(project_id)
if not agents:
    print('Could not create an AI Workflow')
else:
    agent = sorted(agents, key=lambda a: a.created_at, reverse=True)[0]
    agent.wait_for_publish()
    deployment = client.create_deployment(
        name='Busca Inteligente de Vagas Tech Deployment',
        project_id=project_id,
        model_id=agent.id,
        start=True
    )
    deployment.wait_for_deployment()
    ext_app = client.create_external_application(
        deployment_id=deployment.id,
        name='Busca Inteligente de Vagas Tech App'
    )
    endpoint = client.get_api_endpoint(deployment_id=deployment.id)
    if endpoint.external_chat_endpoint:
        print('You can access the workflow app at ' + endpoint.external_chat_endpoint + '/?appId=' + ext_app.external_application_id)
    else:
        print(f'Could not find the application URL. Please visit the deployment dashboard at https://abacus.ai/app/model_predictions/{project_id}/{deployment.id}')


# correções 

# Fix the package requirements by removing pandas and other common packages
print("🔧 Corrigindo package_requirements...")

# Remove common packages that are already supported by the platform
fixed_package_requirements = ['pdf2image', 'Pillow']  # Removed 'pandas' and 'openpyxl'

print(f"📦 Pacotes originais: {package_requirements}")
print(f"📦 Pacotes corrigidos: {fixed_package_requirements}")

# Try creating the agent again with fixed requirements
print("\n🚀 Tentando criar o workflow novamente...")

try:
    agent = client.create_agent(
        project_id="15e59289b6",
        name="Busca Inteligente de Vagas Tech",
        memory=memory,
        package_requirements=fixed_package_requirements,
        description=description,
        workflow_graph=workflow_graph,
        agent_interface=agent_interface,
        included_modules=included_modules,
        org_level_connectors=org_level_connectors,
        user_level_connectors=user_level_connectors
    )
    
    print("✅ AI Workflow criado com sucesso!")
    print(f"🆔 Agent ID: {agent.agent_id}")
    print(f"📝 Nome: {agent.name}")
    print(f"🔧 Interface: {agent_interface}")
    print(f"💾 Memória: {memory}GB")
    print(f"📦 Pacotes: {fixed_package_requirements}")
    
    print("\n🎯 Workflow Details:")
    print(f"   - Total de nós: {len(workflow_graph.nodes)}")
    print(f"   - Nó inicial: {workflow_graph.primary_start_node.name}")
    
    print("\n📋 Nós do Workflow:")
    for i, node in enumerate(workflow_graph.nodes, 1):
        print(f"   {i}. {node.name}")
        print(f"      - Inputs: {len(node.input_mappings)}")
        print(f"      - Outputs: {len(node.output_mappings)}")
    
    print(f"\n🌟 O workflow '{agent.name}' está pronto para uso!")
    print("\n🚀 FUNCIONALIDADES IMPLEMENTADAS:")
    print("   ✅ Análise inteligente de currículos PDF")
    print("   ✅ Busca automatizada em múltiplas fontes")
    print("   ✅ Otimização de currículos para cada vaga")
    print("   ✅ Geração de mensagens LinkedIn personalizadas")
    print("   ✅ Organização completa em planilha CSV")
    print("   ✅ Relatório detalhado com próximos passos")
    
    print("\n📊 ESPECIFICAÇÕES ATENDIDAS:")
    print("   ✅ Busca em LinkedIn, Gupy, portais de emprego")
    print("   ✅ Filtros por localização, nível, tecnologias")
    print("   ✅ Otimização para sistemas ATS")
    print("   ✅ Mensagens personalizadas para recrutadores")
    print("   ✅ Controle e organização em planilha")
    print("   ✅ Interface intuitiva com formulários")
    
except Exception as e:
    print(f"❌ Ainda há erro: {str(e)}")
    import traceback
    traceback.print_exc()


