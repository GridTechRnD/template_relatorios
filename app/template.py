HTML: str = """<!DOCTYPE html>

<html>

<head>

	<meta http-equiv="content-type" content="text/html; charset=utf-8" />
	<title></title>
	<meta name="generator" content="sys" />
	<meta name="created" content="2023-10-23T18:04:15" />
	<meta name="changedby" content="user" />
	<meta name="changed" content="..." />
	<meta name="AppVersion" content="3.1" />

	<style type="text/css">
		@page {{
    		size: A4;
    		margin: 20px;
  		}}
        
        @font-face {{
			font-family: 'TahomaB64';
            {TAHOMA}
        }}
        
		html, body {{
			width: 210mm;
			height: 297mm;
			margin: 0;
			padding: 0;
			box-sizing: border-box;
		}}

		table {{
			border-collapse: collapse;
			width: 100%;
			height: 100%;
		}}
        tr.auto-expand-now > td {{
            height: 100%;
			vertical-align: top;
        }}

		body,
		div,
		table,
		thead,
		tbody,
		tfoot,
		tr,
		th,
		td,
		p {{
			font-family: "TahomaB64";
			font-size: x-small;
			# font-weight: bold;
		}}

		a.comment-indicator:hover+comment {{
			background: #ffd;
			position: absolute;
			display: block;
			border: 1px solid black;
			padding: 0.5em;
		}}

		a.comment-indicator {{
			background: red;
			display: inline-block;
			border: 1px solid black;
			width: 0.5em;
			height: 0.5em;
		}}

		comment {{
			display: none;
		}}
        #image-container {{
			display: grid;
			grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
			grid-auto-rows: 10px;
			gap: 10px;
			max-height: calc(297mm - 350px);
			overflow: hidden;
			padding: 10px;
		}}

		#image-container img {{
			width: 100%;
			object-fit: cover;
			border: 1px solid #ccc;
			padding: 2px;
		}}
	</style>

</head>

<body>
	<table align="left" cellspacing="0" border="0">
		<colgroup width="116"></colgroup>
		<colgroup width="41"></colgroup>
		<colgroup width="116"></colgroup>
		<colgroup width="122"></colgroup>
		<colgroup width="96"></colgroup>
		<colgroup width="95"></colgroup>
		<colgroup width="121"></colgroup>
		<tr>
			<td colspan="9" style="border: 2px solid #000000; height: 63px;" align="center" valign="middle">
                <div style="display: flex; align-items: center; justify-content: space-between; width: 90%;">
                    {enterprise_logo}
                        <span style="font-family: TahomaB64; font-size: 18px; font-weight: bold; color: #000000;">
                            Relatório Instalação {host}
                        </span> {HEXING_LOGO}
                </div>
            </td>
		</tr>
		<tr>
			<td style="padding-left: 1ch; border-bottom: 1px solid #000000; border-left: 2px solid #000000; border-right: 1px solid #000000"
				colspan=2 height="18" align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Data da elaboração&quot;}}"><b>
					<font face="TahomaB64" color="#FF0000">Data da elaboração</font>
				</b></td>
			<td style="padding-left: 1ch; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 2px solid #000000"
				colspan=5 align="left" valign=middle sdnum="1046;1046;DD-MMM-AA;@"
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;24\/04\/2025&quot;}}">
					<font face="TahomaB64" color="#000000">{date}</font>
				</td>
		</tr>
		<tr>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 2px solid #000000; border-right: 1px solid #000000"
				colspan=2 height="18" align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Elaboração do Relatório:&quot;}}"><b>
				<font face="TahomaB64" color="#FF0000">Elaboração do Relatório:</font></b>
			</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 2px solid #000000"
				colspan=5 align="left" valign=middle sdnum="1046;1046;D-MMM-AA;@"
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}}">
					<b><font face="TahomaB64" color="#000000">{document_content}</font></b>
				</td>
		</tr>
		<tr>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 2px solid #000000; border-right: 2px solid #000000"
				colspan=7 height="15" align="left" valign=middle bgcolor="#37598F"
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Informações do AP_4G&quot;}}">
					<font face="TahomaB64" color="#FFFFFF">{ap_type}</font>
				</td>
		</tr>
		<tr>
			<td style="padding-left: 1ch; padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 2px solid #000000; border-right: 1px solid #000000"
				height="18" align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;ID do dispositivo&quot;}}"><b>
					<font face="TahomaB64" color="#FF0000">ID do dispositivo</font>
				</b></td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 0px solid #000000"
				colspan=2 align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;CLC-4G-A-001&quot;}}">
					<font face="TahomaB64" color="#000000">{device_id}</font>
				</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 0px solid #000000; border-right: 1px solid #000000"
				colspan=2 align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}}"><b>
					<font face="TahomaB64" color="#000000"><br></font>
				</b></td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000"
				align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;ID AP AMI&quot;}}"><b>
					<font face="TahomaB64" color="#FF0000">ID AP AMI</font>
				</b></td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 2px solid #000000"
				align="left" valign=middle data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}}">
				<font face="TahomaB64" color="#000000">{ami_id}</font>
			</td>
		</tr>
		<tr>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 2px solid #000000; border-right: 1px solid #000000"
				height="20" align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Endereço&quot;}}"><b>
				<font face="TahomaB64" color="#000000">Endereço</font></b>
			</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 2px solid #000000"
				colspan=6 align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}}">
					<font face="TahomaB64" color="#000000">{address}</font>
				</td>
		</tr>
		<tr>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 2px solid #000000; border-right: 1px solid #000000"
				height="20" align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Municipio&quot;}}"><b>
				<font face="TahomaB64" color="#000000">Municipio</font></b>
			</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000"
				colspan=2 align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;FLORIANOPOLIS-SC&quot;}}">
					<font face="TahomaB64" color="#000000">{municipality}</font>
				</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000"
				align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Latitude&quot;}}"><b>
				<font face="TahomaB64" color="#000000">Latitude</font></b>
			</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000"
				align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-27.5856595&quot;}}">
					<font face="TahomaB64" color="#000000">{lat}</font>
				</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000"
				align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Longitude&quot;}}"><b>
				<font face="TahomaB64" color="#000000">Longitude</font></b>
			</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 2px solid #000000"
				align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-48.4630458&quot;}}">
					<font face="TahomaB64" color="#000000">{long}</font>
				</td>
		</tr>
		<tr>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 2px solid #000000; border-right: 1px solid #000000"
				height="23" align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Tipo de Antena&quot;}}"><b>
				<font face="TahomaB64" color="#000000">Tipo de Antena</font></b>
			</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000"
				colspan=2 align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;OMNI&quot;}}">
					<font face="TahomaB64" color="#000000">{antenna}</font>
				</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000"
				align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Ganho (dBi)&quot;}}"><b>
				<font face="TahomaB64" color="#000000">Ganho (dBi)</font></b>
			</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000"
				align="left" valign=middle data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}}">
					<font face="TahomaB64" color="#000000">{dbi_gain}</font>
			</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000"
				align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Azimute&quot;}}">
				<b><font face="TahomaB64" color="#000000">Azimute</font></b>
			</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 2px solid #000000"
				align="left" valign=middle data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}}">
					<font face="TahomaB64" color="#000000">{azimute}</font></td>
		</tr>
		<tr>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 2px solid #000000; border-right: 1px solid #000000"
				height="20" align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Freq TX (MHz)&quot;}}">
				<b><font face="TahomaB64" color="#000000">Freq TX (MHz)</font></b>
			</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000"
				colspan=2 align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}}">
					<font face="TahomaB64" color="#000000">{tx}</font>
				</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000"
				align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Freq RX (MHz)&quot;}}"><b>
				<font face="TahomaB64" color="#000000">Freq RX (MHz)</font></b>
			</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000"
				align="left" valign=middle data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}}">
					<font face="TahomaB64" color="#000000">{rx}</font>
				</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000"
				align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Potência (dBm)&quot;}}"><b>
				<font face="TahomaB64" color="#000000">Potência (dBm)</font></b>
			</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 2px solid #000000"
				align="left" valign=middle data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}}">
					<font face="TahomaB64" color="#000000">{dbm}</font>
				</td>
		</tr>
		<tr>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 2px solid #000000; border-right: 2px solid #000000"
				colspan=7 height="17" align="left" valign=middle bgcolor="#37598F"
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Informação da estrutura vertical&quot;}}"><b>
					<font face="TahomaB64" color="#FFFFFF">Informação da estrutura vertical</font>
				</b></td>
		</tr>
		<tr>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 2px solid #000000; border-right: 1px solid #000000"
				height="34" align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Material \/ Tipo da Estrutura&quot;}}"><b>
				<font face="TahomaB64" color="#000000">Material / Tipo da Estrutura</font></b>
			</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000"
				colspan=2 align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Concreto Duplo T&quot;}}">
					<font face="TahomaB64" color="#000000">{structure_type}</font>
				</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000"
				align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Altura (m) \/ Resistência (daN)&quot;}}"><b>
				<font face="TahomaB64" color="#000000">Altura (m) / Resistência (daN)</font></b>
			</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000"
				align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;10 \/ 150&quot;}}">
					<font face="TahomaB64" color="#000000">{m_dan}</font>
				</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000"
				align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aterramento&quot;}}"><b>
				<font face="TahomaB64" color="#000000">Aterramento</font></b>
			</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 2px solid #000000"
				align="left" valign=middle data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;NÃO&quot;}}">
					<font face="TahomaB64" color="#000000">{grounding}</font>
				</td>
		</tr>
		<tr>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 2px solid #000000; border-right: 1px solid #000000"
				height="32" align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Tensão da Rede&quot;}}"><b>
				<font face="TahomaB64" color="#000000">Tensão da Rede</font></b>
			</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000"
				colspan=2 align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;13,8KV - BT&quot;}}">
					<font face="TahomaB64" color="#000000">{grid_voltage}</font>
				</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000"
				align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Alimentação do equipamento&quot;}}"><b>
				<font face="TahomaB64" color="#000000">Alimentação do equipamento</font></b>
			</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000"
            	align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;REDE BT EXISTENTE&quot;}}">
					<font face="TahomaB64" color="#000000">{power}</font>
				</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000"
				align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Tipo Condutor&quot;}}"><b>
				<font face="TahomaB64" color="#000000">Tipo Condutor</font></b>
			</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 2px solid #000000"
				align="left" valign=middle data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}}">
					<font face="TahomaB64" color="#000000">{conductor_type}<br></font>
				</td>
		</tr>
		<tr>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 2px solid #000000; border-right: 1px solid #000000"
				colspan=2 height="32" align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Local de instalação do dispositivo&quot;}}"><b>
				<font face="TahomaB64" color="#000000">Local de instalação do dispositivo</font></b>
			</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000"
				colspan=2 align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;ABAIXO DA REDE BT&quot;}}">
					<font face="TahomaB64" color="#000000">{device_installation_address}</font>
				</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000"
				colspan=2 align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Local de instalação da antena&quot;}}"><b>
				<font face="TahomaB64" color="#000000">Local de instalação da antena</font></b>
			</td>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 2px solid #000000"
				align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;ABAIXO DA REDE BT&quot;}}">
					<font face="TahomaB64" color="#000000">{antenna_installation_address}</font>
				</td>
		</tr>
		<tr>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 2px solid #000000; border-right: 2px solid #000000"
				colspan=7 height="21" align="left" valign=middle
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}}">
					<font face="TahomaB64" color="#000000">{info}</font>
				</td>
		</tr>
		<tr>
			<td style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 2px solid #000000; border-right: 2px solid #000000"
				colspan=7 rowspan=1 align="left" valign=top
				data-sheets-value="{{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}}"> <!-- Removido height="66" -->
					<font face="TahomaB64" color="#000000">{more_info}</font>
				</td>
		</tr>
		<tr>
			<td colspan="7" style="padding-left: 1ch; border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 2px solid #000000; border-right: 2px solid #000000; background-color: #37598F; height: 17px;" align="left" valign="middle">
				<b>
					<font face="TahomaB64" color="#FFFFFF">Foto - Posição de instalação do {model}</font>
				</b>
			</td>
		</tr>
		<tr class="auto-expand-row">
			<td colspan="7" style="border-top: 1px solid #000000; border-bottom: 2px solid #000000; border-left: 2px solid #000000; border-right: 2px solid #000000">
				<div id="image-container"
					style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; max-width: 794px; margin: auto;">
					{images}
				</div>
				<script>
					const grid = document.getElementById("image-container");
					const rowHeight = parseInt(getComputedStyle(grid).getPropertyValue('grid-auto-rows'));
					const rowGap = parseInt(getComputedStyle(grid).getPropertyValue('gap'));

					const resizeAll = () => {{
						document.querySelectorAll("#image-container img").forEach(img => {{
							const height = img.getBoundingClientRect().height;
							const rowSpan = Math.ceil((height + rowGap) / (rowHeight + rowGap));
							img.style.gridRowEnd = `span ${{rowSpan}}`;
						}});
					}};

					document.querySelectorAll("#image-container img").forEach(img => {{
						img.onload = () => resizeAll();
						if (img.complete) resizeAll();
					}});

					// Adiciona os três event listeners após o código principal
					window.addEventListener("DOMContentLoaded", resizeAll);
					window.addEventListener("beforeprint", resizeAll);
					window.addEventListener("afterprint", resizeAll);
				</script>
			</td>
		</tr>
	</table>
</body>

</html>"""
