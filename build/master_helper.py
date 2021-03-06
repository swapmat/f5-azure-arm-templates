#/usr/bin/python env
import sys
import os
import httplib

def parameter_initialize(data):
    """ Set default parameters, as well as all optional ones in a specific order """
    data['parameters']['numberOfInstances'] = "OPTIONAL"
    data['parameters']['vmScaleSetMinCount'] = "OPTIONAL"
    data['parameters']['vmScaleSetMaxCount'] = "OPTIONAL"
    data['parameters']['scaleOutThroughput'] = "OPTIONAL"
    data['parameters']['scaleInThroughput'] = "OPTIONAL"
    data['parameters']['scaleTimeWindow'] = "OPTIONAL"
    data['parameters']['adminUsername'] = "MANDATORY"
    data['parameters']['adminPassword'] = "MANDATORY"
    data['parameters']['dnsLabel'] = "MANDATORY"
    data['parameters']['instanceName'] = "OPTIONAL"
    data['parameters']['instanceType'] = "MANDATORY"
    data['parameters']['imageName'] = "MANDATORY"
    data['parameters']['imageName'] = "OPTIONAL"
    data['parameters']['bigIpVersion'] = "MANDATORY"
    data['parameters']['licenseKey1'] = "OPTIONAL"
    data['parameters']['licenseKey2'] = "OPTIONAL"
    data['parameters']['licensedBandwidth'] = "OPTIONAL"
    data['parameters']['numberOfExternalIps'] = "OPTIONAL"
    data['parameters']['vnetAddressPrefix'] = "OPTIONAL"
    data['parameters']['vnetName'] = "OPTIONAL"
    data['parameters']['vnetResourceGroupName'] = "OPTIONAL"
    data['parameters']['mgmtSubnetName'] = "OPTIONAL"
    data['parameters']['mgmtIpAddressRangeStart'] = "OPTIONAL"
    data['parameters']['mgmtIpAddress'] = "OPTIONAL"
    data['parameters']['externalSubnetName'] = "OPTIONAL"
    data['parameters']['externalIpSelfAddressRangeStart'] = "OPTIONAL"
    data['parameters']['externalIpAddressRangeStart'] = "OPTIONAL"
    data['parameters']['externalIpAddressRangeStart'] = "OPTIONAL"
    data['parameters']['internalSubnetName'] = "OPTIONAL"
    data['parameters']['internalIpAddressRangeStart'] = "OPTIONAL"
    data['parameters']['internalIpAddress'] = "OPTIONAL"
    data['parameters']['solutionDeploymentName'] = "OPTIONAL"
    data['parameters']['applicationProtocols'] = "OPTIONAL"
    data['parameters']['applicationAddress'] = "OPTIONAL"
    data['parameters']['applicationServiceFqdn'] = "OPTIONAL"
    data['parameters']['applicationPort'] = "OPTIONAL"
    data['parameters']['applicationSecurePort'] = "OPTIONAL"
    data['parameters']['sslCert'] = "OPTIONAL"
    data['parameters']['sslPswd'] = "OPTIONAL"
    data['parameters']['applicationType'] = "OPTIONAL"
    data['parameters']['blockingLevel'] = "OPTIONAL"
    data['parameters']['customPolicy'] = "OPTIONAL"
    data['parameters']['tenantId'] = "OPTIONAL"
    data['parameters']['clientId'] = "OPTIONAL"
    data['parameters']['servicePrincipalSecret'] = "OPTIONAL"
    data['parameters']['managedRoutes'] = "OPTIONAL"
    data['parameters']['routeTableTag'] = "OPTIONAL"
    data['parameters']['ntpServer'] = "MANDATORY"
    data['parameters']['timeZone'] = "MANDATORY"
    data['parameters']['restrictedSrcAddress'] = "MANDATORY"
    data['parameters']['tagValues'] = "MANDATORY"

    return data

def variable_initialize(data):
    """ Set default variables, as well as all optional ones in a specific order """
    data['variables']['bigIpNicPortMap'] = { "1": { "Port": "[parameters('bigIpVersion')]" }, "2": { "Port": "443" }, "3": { "Port": "443" }, "4": { "Port": "443" }, "5": { "Port": "443" }, "6": { "Port": "443" } }
    data['variables']['bigIpVersionPortMap'] = "MANDATORY"
    data['variables']['apiVersion'] = "2015-06-15"
    data['variables']['computeApiVersion'] = "2015-06-15"
    data['variables']['networkApiVersion'] = "2015-06-15"
    data['variables']['storageApiVersion'] = "2015-06-15"
    data['variables']['insightsApiVersion'] = "2015-04-01"
    data['variables']['location'] = "[resourceGroup().location]"
    data['variables']['subscriptionID'] = "[subscription().subscriptionId]"
    data['variables']['resourceGroupName'] = "[resourceGroup().name]"
    data['variables']['singleQuote'] = "'"
    data['variables']['f5CloudLibsTag'] = "MANDATORY"
    data['variables']['f5CloudLibsAzureTag'] = "MANDATORY"
    data['variables']['f5NetworksTag'] = "MANDATORY"
    data['variables']['f5CloudIappsTag'] = "MANDATORY"
    data['variables']['f5NetworksSolutionScripts'] = "OPTIONAL"
    data['variables']['verifyHash'] = "MANDATORY"
    data['variables']['installCloudLibs'] = "MANDATORY"
    data['variables']['dnsLabel'] = "[toLower(parameters('dnsLabel'))]"
    data['variables']['imageNameToLower'] = "[toLower(parameters('imageName'))]"
    data['variables']['skuToUse'] = "MANDATORY"
    data['variables']['offerToUse'] = "MANDATORY"
    data['variables']['bigIpNicPortValue'] = "MANDATORY"
    data['variables']['bigIpMgmtPort'] = "[variables('bigIpVersionPortMap')[variables('bigIpNicPortValue')].Port]"
    data['variables']['instanceName'] = "OPTIONAL"
    data['variables']['availabilitySetName'] = "[concat(variables('dnsLabel'), '-avset')]"
    data['variables']['virtualNetworkName'] = "[concat(variables('dnsLabel'), '-vnet')]"
    data['variables']['vnetId'] = "[resourceId('Microsoft.Network/virtualNetworks', variables('virtualNetworkName'))]"
    data['variables']['vnetAddressPrefix'] = "OPTIONAL"
    data['variables']['publicIPAddressType'] = "Static"
    data['variables']['mgmtPublicIPAddressName'] = "[concat(variables('dnsLabel'), '-mgmt-pip')]"
    data['variables']['mgmtPublicIPAddressId'] = "[resourceId('Microsoft.Network/publicIPAddresses', variables('mgmtPublicIPAddressName'))]"
    data['variables']['mgmtNsgID'] = "[resourceId('Microsoft.Network/networkSecurityGroups/',concat(variables('dnsLabel'),'-mgmt-nsg'))]"
    data['variables']['mgmtNicName'] = "[concat(variables('dnsLabel'), '-mgmt')]"
    data['variables']['mgmtSubnetName'] = "[concat(variables('dnsLabel'),'-mgmt-subnet')]"
    data['variables']['mgmtSubnetId'] = "[concat(variables('vnetId'), '/subnets/', variables('mgmtSubnetName'))]"
    data['variables']['mgmtSubnetPrefix'] = "OPTIONAL"
    data['variables']['mgmtSubnetPrivateAddressPrefixArray'] = "OPTIONAL"
    data['variables']['mgmtSubnetPrivateAddressPrefix'] = "OPTIONAL"
    data['variables']['mgmtSubnetPrivateAddressSuffixInt'] = "OPTIONAL"
    data['variables']['mgmtSubnetPrivateAddressSuffix'] = "OPTIONAL"
    data['variables']['mgmtSubnetPrivateAddress'] = "OPTIONAL"
    data['variables']['mgmtSubnetPrivateAddress1'] = "OPTIONAL"
    data['variables']['extSelfPublicIpAddressNamePrefix'] = "OPTIONAL"
    data['variables']['extSelfPublicIpAddressIdPrefix'] = "OPTIONAL"
    data['variables']['extpublicIPAddressNamePrefix'] = "OPTIONAL"
    data['variables']['extPublicIPAddressIdPrefix'] = "OPTIONAL"
    data['variables']['extNsgID'] = "OPTIONAL"
    data['variables']['extNicName'] = "OPTIONAL"
    data['variables']['extSubnetName'] = "OPTIONAL"
    data['variables']['extSubnetPrefix'] = "OPTIONAL"
    data['variables']['extSubnetId'] = "OPTIONAL"
    data['variables']['extSubnetSelfPrivateAddressPrefixArray'] = "OPTIONAL"
    data['variables']['extSubnetSelfPrivateAddressPrefix'] = "OPTIONAL"
    data['variables']['extSubnetSelfPrivateAddressSuffixInt'] = "OPTIONAL"
    data['variables']['extSubnetSelfPrivateAddressSuffix'] = "OPTIONAL"
    data['variables']['extSubnetPrivateAddress'] = "OPTIONAL"
    data['variables']['extSubnetPrivateAddress1'] = "OPTIONAL"
    data['variables']['extSubnetPrivateAddressPrefixArray'] = "OPTIONAL"
    data['variables']['extSubnetPrivateAddressPrefix'] = "OPTIONAL"
    data['variables']['extSubnetPrivateAddressSuffixInt'] = "OPTIONAL"
    data['variables']['extSubnetPrivateAddressSuffix0'] = "OPTIONAL"
    data['variables']['extSubnetPrivateAddressSuffix1'] = "OPTIONAL"
    data['variables']['extSubnetPrivateAddressSuffix2'] = "OPTIONAL"
    data['variables']['extSubnetPrivateAddressSuffix3'] = "OPTIONAL"
    data['variables']['extSubnetPrivateAddressSuffix4'] = "OPTIONAL"
    data['variables']['extSubnetPrivateAddressSuffix5'] = "OPTIONAL"
    data['variables']['extSubnetPrivateAddressSuffix6'] = "OPTIONAL"
    data['variables']['extSubnetPrivateAddressSuffix7'] = "OPTIONAL"
    data['variables']['intNicName'] = "OPTIONAL"
    data['variables']['intSubnetName'] = "OPTIONAL"
    data['variables']['intSubnetPrefix'] = "OPTIONAL"
    data['variables']['intSubnetId'] = "OPTIONAL"
    data['variables']['intSubnetPrivateAddress'] = "OPTIONAL"
    data['variables']['intSubnetPrivateAddress1'] = "OPTIONAL"
    data['variables']['intSubnetPrivateAddressPrefixArray'] = "OPTIONAL"
    data['variables']['intSubnetPrivateAddressPrefix'] = "OPTIONAL"
    data['variables']['intSubnetPrivateAddressSuffixInt'] = "OPTIONAL"
    data['variables']['intSubnetPrivateAddressSuffix'] = "OPTIONAL"
    data['variables']['extSubnetRef'] = "OPTIONAL"
    data['variables']['intSubnetRef'] = "OPTIONAL"
    data['variables']['numberOfExternalIps'] = "OPTIONAL"
    data['variables']['selfIpconfigArray'] = "OPTIONAL"
    data['variables']['extIpconfigArray'] = "OPTIONAL"
    data['variables']['ipAddress'] = "OPTIONAL"
    data['variables']['loadBalancerName'] = "OPTIONAL"
    data['variables']['deviceNamePrefix'] = "OPTIONAL"
    data['variables']['lbID'] = "OPTIONAL"
    data['variables']['frontEndIPConfigID'] = "OPTIONAL"
    data['variables']['vmssName'] = "OPTIONAL"
    data['variables']['25m'] = "OPTIONAL"
    data['variables']['200m'] = "OPTIONAL"
    data['variables']['1g'] = "OPTIONAL"
    data['variables']['scaleOutCalc'] = "OPTIONAL"
    data['variables']['scaleInCalc'] = "OPTIONAL"
    data['variables']['scaleOutNetworkBits'] = "OPTIONAL"
    data['variables']['scaleInNetworkBits'] = "OPTIONAL"
    data['variables']['scaleOutNetworkBytes'] = "OPTIONAL"
    data['variables']['scaleInNetworkBytes'] = "OPTIONAL"
    data['variables']['timeWindow'] = "OPTIONAL"
    data['variables']['lbTcpProbeNameHttp'] = "OPTIONAL"
    data['variables']['lbTcpProbeIdHttp'] = "OPTIONAL"
    data['variables']['lbTcpProbeNameHttps'] = "OPTIONAL"
    data['variables']['lbTcpProbeIdHttps'] = "OPTIONAL"
    data['variables']['httpBackendPort'] = "OPTIONAL"
    data['variables']['httpsBackendPort'] = "OPTIONAL"
    data['variables']['commandArgs'] = "OPTIONAL"
    # Add storage array variables at the end
    data['variables']['instanceTypeMap'] = { "Standard_A3": { "storageAccountType": "Standard_LRS" }, "Standard_A4": { "storageAccountType": "Standard_LRS" }, "Standard_A5": { "storageAccountType": "Standard_LRS" }, "Standard_A6": { "storageAccountType": "Standard_LRS" }, "Standard_A7": { "storageAccountType": "Standard_LRS" }, "Standard_D2": { "storageAccountType": "Standard_LRS" }, "Standard_D3": { "storageAccountType": "Standard_LRS" }, "Standard_D4": { "storageAccountType": "Standard_LRS" }, "Standard_D11": { "storageAccountType": "Standard_LRS" }, "Standard_D12": { "storageAccountType": "Standard_LRS" }, "Standard_D13": { "storageAccountType": "Standard_LRS" }, "Standard_D14": { "storageAccountType": "Standard_LRS" }, "Standard_D2_v2": { "storageAccountType": "Standard_LRS" }, "Standard_D3_v2": { "storageAccountType": "Standard_LRS" }, "Standard_D4_v2": { "storageAccountType": "Standard_LRS" }, "Standard_D5_v2": { "storageAccountType": "Standard_LRS" }, "Standard_D11_v2": { "storageAccountType": "Standard_LRS" }, "Standard_D12_v2": { "storageAccountType": "Standard_LRS" }, "Standard_D13_v2": { "storageAccountType": "Standard_LRS" }, "Standard_D14_v2": { "storageAccountType": "Standard_LRS" }, "Standard_F2": { "storageAccountType": "Standard_LRS" }, "Standard_F4": { "storageAccountType": "Standard_LRS" }, "Standard_G1": { "storageAccountType": "Standard_LRS" }, "Standard_G2": { "storageAccountType": "Standard_LRS" }, "Standard_G3": { "storageAccountType": "Standard_LRS" }, "Standard_G4": { "storageAccountType": "Standard_LRS" }, "Standard_G5": { "storageAccountType": "Standard_LRS" }, "Standard_DS1": { "storageAccountType": "Premium_LRS" }, "Standard_DS2": { "storageAccountType": "Premium_LRS" }, "Standard_DS3": { "storageAccountType": "Premium_LRS" }, "Standard_DS4": { "storageAccountType": "Premium_LRS" }, "Standard_DS11": { "storageAccountType": "Premium_LRS" }, "Standard_DS12": { "storageAccountType": "Premium_LRS" }, "Standard_DS13": { "storageAccountType": "Premium_LRS" }, "Standard_DS14": { "storageAccountType": "Premium_LRS" }, "Standard_DS1_v2": { "storageAccountType": "Premium_LRS" }, "Standard_DS2_v2": { "storageAccountType": "Premium_LRS" }, "Standard_DS3_v2": { "storageAccountType": "Premium_LRS" }, "Standard_DS4_v2": { "storageAccountType": "Premium_LRS" }, "Standard_DS5_v2": { "storageAccountType": "Premium_LRS" }, "Standard_DS11_v2": { "storageAccountType": "Premium_LRS" }, "Standard_DS12_v2": { "storageAccountType": "Premium_LRS" }, "Standard_DS13_v2": { "storageAccountType": "Premium_LRS" }, "Standard_DS14_v2": { "storageAccountType": "Premium_LRS" }, "Standard_DS15_v2": { "storageAccountType": "Premium_LRS" }, "Standard_GS1": { "storageAccountType": "Premium_LRS" }, "Standard_GS2": { "storageAccountType": "Premium_LRS" }, "Standard_GS3": { "storageAccountType": "Premium_LRS" }, "Standard_GS4": { "storageAccountType": "Premium_LRS" }, "Standard_GS5": { "storageAccountType": "Premium_LRS" } }
    data['variables']['newStorageAccountName'] = "[concat(uniquestring(resourceGroup().id), 'stor')]"
    data['variables']['storageAccountType'] = "[variables('instanceTypeMap')[parameters('instanceType')].storageAccountType]"
    data['variables']['newDataStorageAccountName'] = "[concat(uniquestring(resourceGroup().id), 'data000')]"
    data['variables']['dataStorageAccountType'] = "Standard_LRS"

    return data

def template_check(data, resource):
    """ Remove extra optional resources(variables, parameters, etc...), also check if mandatory parameter was not filled in """
    for var in data[resource]:
        if data[resource][var] == "OPTIONAL":
            data[resource].pop(var)
        elif data[resource][var] == "MANDATORY":
            raise Exception('Mandatory parameter was not filled in, exiting...')
            sys.exit(1)
    return data

def verify_hash(url):
    """ Download latest verifyHash to be used by the templates """
    # Parse out url information needed
    (protocol, host_path) = url.split('//')
    (host, path) = host_path.split('/', 1)
    path = '/' + path
    if url.startswith('https'):
        conn = httplib.HTTPSConnection(host)
    else:
        conn = httplib.HTTPConnection(host)
    # Make HTTP Request
    conn.request('GET', path)
    response = conn.getresponse()
    if response.status == 200:
        pass
    else:
        raise Exception("Unable to download verify hash file, HTTP Error Response: %s"  % response.msg)
    # HTTP Call MIGHT include trailing \n, remove that
    response_str = response.read()
    if response_str[-1:] == '\n':
        response_str = response_str[:-1]
    return response_str