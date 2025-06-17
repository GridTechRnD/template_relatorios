CELESC_TEX: str = r"""\documentclass{{article}}
\usepackage[a4paper,margin=0.15cm]{{geometry}}
\usepackage{{array}}
\usepackage{{tabularx}}
\usepackage{{graphicx}}
\usepackage{{fontspec}}
\usepackage[table]{{xcolor}}

\setmainfont[
    Path=/media/fonts/,
    Extension=.ttf,
    UprightFont = Tahoma-Regular,
    BoldFont = Tahoma-Bold
]{{Tahoma}}

\setlength{{\arrayrulewidth}}{{0.7mm}}
\renewcommand{{\arraystretch}}{{1.5}}

\definecolor{{hexingblue}}{{RGB}}{{55, 89, 143}}

\newcommand{{\customheader}}{{%
    \noindent
    \begin{{minipage}}[c]{{\textwidth}}
        \raggedright
        \raisebox{{-.5\height}}{{
        \setlength{{\fboxsep}}{{0.3cm}}
        \setlength{{\fboxrule}}{{0pt}}
        \fbox{{\includegraphics[height=1.1cm]{{  {enterprise_logo} }}}}}}
        \hfill
        \makebox[0pt][c]{{\raisebox{{-1\height}}{{\fontsize{{16pt}}{{22pt}}\selectfont \textbf{{Relatório Instalação  {host} }}}}}}
        \hfill
        \raggedleft
        \raisebox{{-.5\height}}{{
        \setlength{{\fboxsep}}{{0.3cm}}
        \setlength{{\fboxrule}}{{0pt}}
        \fbox{{\includegraphics[height=1.3cm]{{ {hexing_logo} }}}}}}
    \end{{minipage}}
    \vspace{{0.1cm}}
    \vspace{{0.1cm}}
}}

\begin{{document}}

\customheader

\noindent
\begin{{tabularx}}{{\textwidth}}{{
  |>{{\arraybackslash}}X
  >{{\arraybackslash}}X
  >{{\arraybackslash}}X
  >{{\arraybackslash}}X
  >{{\arraybackslash}}X
  |>{{\arraybackslash}}X|
  }}
  \hline
  \multicolumn{{2}}{{|l}}{{Data da elaboração}} &
  \multicolumn{{4}}{{|l|}}{{\textbf{{ {date} }}}} \\
  \hline
  \multicolumn{{2}}{{|l}}{{Elaboração do Relatório}} &
  \multicolumn{{4}}{{|l|}}{{\textbf{{ {document_content} }}}} \\
  \hline
  \multicolumn{{6}}{{|l|}}{{\cellcolor{{hexingblue}}{{\color{{white}} \textbf{{ID do Dispositivo de Rede}}}}}} \\
  \hline
  \multicolumn{{2}}{{|l}}{{\textbf{{ID do dispositivo}}}} &
  \multicolumn{{2}}{{|l|}}{{\textbf{{ {device_id} }}}} &
  ID AP AMI & \textbf{{ {ami_id} }} \\
  \hline
  \multicolumn{{1}}{{|l|}}{{Endereço}} &
  \multicolumn{{5}}{{p{{14cm}}|}}{{\centering \textbf{{ {address} }}}} \\
  \hline
  \multicolumn{{1}}{{|l|}}{{Municipio}} &
  \multicolumn{{1}}{{c|}}{{\textbf{{ {municipality} }}}} &
  \multicolumn{{1}}{{c|}}{{Latitude}} &
  \multicolumn{{1}}{{c|}}{{\textbf{{ {lat} }}}} &
  \multicolumn{{1}}{{c|}}{{Longitude}}
  & \multicolumn{{1}}{{c|}}{{\textbf{{ {long} }}}} \\
  \hline
  \multicolumn{{1}}{{|l|}}{{Tipo de Antena}} &
  \multicolumn{{1}}{{c|}}{{\textbf{{ {antenna} }}}} &
  \multicolumn{{1}}{{c|}}{{Ganho (dBi)}} &
  \multicolumn{{1}}{{c|}}{{\textbf{{ {dbi_gain} }}}} &
  \multicolumn{{1}}{{c|}}{{Azimute}} &
  \multicolumn{{1}}{{c|}}{{\textbf{{ {azimute} }}}} \\
  \hline
  \multicolumn{{1}}{{|l|}}{{Freq TX (MHz)}} &
  \multicolumn{{1}}{{c|}}{{\textbf{{ {tx} }}}} &
  \multicolumn{{1}}{{c|}}{{Freq RX (MHz)}} &
  \multicolumn{{1}}{{c|}}{{\textbf{{ {rx} }}}} &
  \multicolumn{{1}}{{c|}}{{Potência (dBm)}} &
  \multicolumn{{1}}{{c|}}{{\textbf{{ {dbm} }}}} \\
  \hline
  \multicolumn{{6}}{{|l|}}{{\cellcolor{{hexingblue}}{{\color{{white}} \textbf{{Informação da estrutura vertical}}}}}} \\
  \hline
  \multicolumn{{1}}{{|p{{2.8cm}}|}}{{Material / Tipo da Estrutura}} &
  \multicolumn{{1}}{{c|}}{{\textbf{{ {structure_type} }}}} &
  \multicolumn{{1}}{{p{{3cm}}|}}{{Altura (m) / Resistência (daN)}} &
  \multicolumn{{1}}{{c|}}{{\textbf{{ {m_dan} }}}} &
  \multicolumn{{1}}{{c|}}{{Aterramento}} &
  \multicolumn{{1}}{{c|}}{{\textbf{{ {grounding} }}}} \\
  \hline
  \multicolumn{{1}}{{|l|}}{{Tensão da Rede}} &
  \multicolumn{{1}}{{c|}}{{\textbf{{ {grid_voltage} }}}} &
  \multicolumn{{1}}{{p{{3cm}}|}}{{Alimentação do equipamento}} &
  \multicolumn{{1}}{{c|}}{{\textbf{{ {power} }}}} &
  \multicolumn{{1}}{{l|}}{{Tipo Condutor}} &
  \multicolumn{{1}}{{c|}}{{\textbf{{ {conductor_type} }}}} \\
  \hline
  \multicolumn{{2}}{{|p{{3cm}}|}}{{Local de instalação do dispositivo}} &
  \multicolumn{{1}}{{c|}}{{\textbf{{ {device_installation_address} }}}} &
  \multicolumn{{2}}{{p{{3cm}}|}}{{Local de instalação da antena}} &
  \multicolumn{{1}}{{c|}}{{\textbf{{ {antenna_installation_address} }}}} &
  \hline
  \multicolumn{{1}}{{|l|}}{{Observações}} &
  \multicolumn{{5}}{{l|}}{{\textbf{{ {info} }}}} \\
  \hline
  \multicolumn{{6}}{{|p{{15cm}}|}}{{\textbf{{ {more_info} }}}} \\
  \hline
  \multicolumn{{6}}{{|l|}}{{\cellcolor{{hexingblue}}{{\color{{white}} \textbf{{Foto - Posição de instalação do {host} }}}}}} \\
  \hline
  \multicolumn{{6}}{{|c|}}{{%
    \begin{{minipage}}{{\dimexpr\textwidth-2\tabcolsep-2\arrayrulewidth\relax}}
      \setlength{{\parindent}}{{0pt}}%
      \begin{{minipage}}[t]{{0.48\textwidth}}
        \raisebox{{-1\height}}{{%
          \setlength{{\fboxsep}}{{2mm}}%
          \setlength{{\fboxrule}}{{0pt}}%
          \fbox{{\includegraphics[width=\linewidth, scale=2, height=14cm,keepaspectratio]{{ {temp_image1} }}}}%
        }}
      \end{{minipage}}\hfill
      \begin{{minipage}}[t]{{0.48\textwidth}}
        \raisebox{{-1\height}}{{%
          \setlength{{\fboxsep}}{{2mm}}%
          \setlength{{\fboxrule}}{{0pt}}%
          \fbox{{\includegraphics[width=\linewidth,height=6.9cm,keepaspectratio]{{ {temp_image2} }}}}%
        }}\\[1mm]
        \raisebox{{-1\height}}{{%
          \setlength{{\fboxsep}}{{2mm}}%
          \setlength{{\fboxrule}}{{0pt}}%
          \fbox{{\includegraphics[width=\linewidth,height=6.9cm,keepaspectratio]{{ {temp_image3} }}}}%
        }}
      \end{{minipage}}
    \end{{minipage}}%
  }} \\
\hline
\end{{tabularx}}
\end{{document}}
"""

CPFL_TEX: str = r"""\documentclass{{article}}
\usepackage[a4paper,margin=0.15cm]{{geometry}}
\usepackage{{array}}
\usepackage{{tabularx}}
\usepackage{{graphicx}}
\usepackage{{fontspec}}
\usepackage[table]{{xcolor}}

\setmainfont[
    Path=/media/fonts/,
    Extension=.ttf,
    UprightFont = Tahoma-Regular,
    BoldFont = Tahoma-Bold
]{{Tahoma}}

\setlength{{\arrayrulewidth}}{{0.7mm}}
\renewcommand{{\arraystretch}}{{1.5}}

\definecolor{{hexingblue}}{{RGB}}{{55, 89, 143}}

% Define a nova header
\newcommand{{\customheader}}{{%
    \noindent% No indent for the minipage
    \begin{{minipage}}[c]{{\textwidth}}%
        \raggedright% Align content to the left within its space
        \raisebox{{-.5\height}}{{%
        \setlength{{\fboxsep}}{{0.3cm}}%
        \setlength{{\fboxrule}}{{0pt}}%
        \fbox{{\includegraphics[height=1.1cm]{{ {enterprise_logo} }}}}}}
        \hfill
        \makebox[0pt][c]{{\raisebox{{-1\height}}{{\fontsize{{16pt}}{{22pt}}\selectfont \textbf{{Relatório Instalação {host} }}}}}}
        \hfill
        \raggedleft
        \raisebox{{-.5\height}}{{%
        \setlength{{\fboxsep}}{{0.3cm}}%
        \setlength{{\fboxrule}}{{0pt}}%
        \fbox{{\includegraphics[height=1.3cm]{{ {hexing_logo} }}}}}}
    \end{{minipage}}%
    \vspace{{0.1cm}}
    \vspace{{0.1cm}}
}}

\begin{{document}}

\customheader

\noindent
\begin{{tabularx}}{{\textwidth}}{{
  |>{{\arraybackslash}}X
  >{{\arraybackslash}}X
  >{{\arraybackslash}}X
  >{{\arraybackslash}}X
  >{{\arraybackslash}}X
  |>{{\arraybackslash}}X|
  }}
  \hline
  \multicolumn{{2}}{{|l}}{{Data da elaboração}}                       & \multicolumn{{4}}{{|l|}}{{\textbf{{ {date} }}}}                                                                                                                                                                           \\
  \hline
  \multicolumn{{2}}{{|l}}{{Elaboração do Relatório}}                  & \multicolumn{{4}}{{|l|}}{{\textbf{{ {document_content} }}}}                                                                                                                                                                                                  \\
  \hline
  \multicolumn{{6}}{{|l|}}{{\cellcolor{{hexingblue}}{{\color{{white}} \textbf{{ID do Dispositivo de Rede}}}}}}                                                                                                                                                                                                        \\
  \hline
  \multicolumn{{2}}{{|l}}{{\textbf{{ID do dispositivo}}}}               & \multicolumn{{2}}{{|l|}}{{\textbf{{ {device_id} }}}}                        & PS                                                       & \textbf{{ {ps_id} }}                                                                                               \\
  \hline
  \multicolumn{{1}}{{|l|}}{{Endereço}} &
  \multicolumn{{5}}{{p{{14cm}}|}}{{\centering \textbf{{ {address} }}}} \\
  \hline
  \multicolumn{{1}}{{|l|}}{{Municipio}}                               & \multicolumn{{1}}{{c|}}{{\textbf{{ {municipality} }}}}                         & \multicolumn{{1}}{{c|}}{{Latitude}}                            & \multicolumn{{1}}{{c|}}{{\textbf{{ {lat} }}}} & \multicolumn{{1}}{{c|}}{{Longitude}}   & \multicolumn{{1}}{{c|}}{{\textbf{{ {long} }}}} \\
  \hline
  \multicolumn{{1}}{{|l|}}{{Tipo de Antena}}                          & \multicolumn{{1}}{{c|}}{{\textbf{{ {antenna} }}}}                         & \multicolumn{{1}}{{c|}}{{Ganho (dBi)}}                         & \multicolumn{{1}}{{c|}}{{\textbf{{ {dbi_gain} }}}} & \multicolumn{{1}}{{c|}}{{Device Mode}} & \multicolumn{{1}}{{c|}}{{\textbf{{ {device_mode} }}}} \\
  \hline
  \multicolumn{{1}}{{|l|}}{{Operadora 4G}}                            & \multicolumn{{1}}{{c|}}{{\textbf{{ {provider} }}}}                         & \multicolumn{{1}}{{c|}}{{Intensidade sinal}}                   & \multicolumn{{1}}{{c|}}{{\textbf{{ {signal_power} }}}} & \multicolumn{{1}}{{c|}}{{Velocidade}}  & \multicolumn{{1}}{{c|}}{{\textbf{{ {speed} }}}} \\
  \hline
  \multicolumn{{6}}{{|l|}}{{\cellcolor{{hexingblue}}{{\color{{white}} \textbf{{Informação da estrutura vertical}}}}}}                                                                                                                                                                                                 \\
  \hline
  \multicolumn{{1}}{{|p{{2.8cm}}|}}{{Material / Tipo da Estrutura}}     & \multicolumn{{1}}{{c|}}{{\textbf{{ {structure_type} }}}}                         & \multicolumn{{1}}{{p{{3cm}}|}}{{Altura (m) / Resistência (daN)}} & \multicolumn{{1}}{{c|}}{{\textbf{{ {m_dan} }}}} & \multicolumn{{1}}{{c|}}{{Aterramento}} & \multicolumn{{1}}{{c|}}{{\textbf{{ {grounding} }}}} \\
  \hline
  \multicolumn{{1}}{{|l|}}{{Tensão da Rede}}                          & \multicolumn{{1}}{{c|}}{{\textbf{{ {grid_voltage} }}}}                         & \multicolumn{{1}}{{p{{3cm}}|}}{{Alimentação do equipamento}}     & \multicolumn{{3}}{{c|}}{{\textbf{{ {power} }}}}                                                                          \\
  \hline
  \multicolumn{{2}}{{|p{{3cm}}|}}{{Local de instalação do dispositivo}} & \multicolumn{{2}}{{c|}}{{\textbf{{ {device_installation_address} }}}}                         & \multicolumn{{2}}{{l|}}{{}}                                                                                                                                                   \\
  \hline
  \multicolumn{{1}}{{|l|}}{{Observações}}                             & \multicolumn{{5}}{{l|}}{{\textbf{{ {info} }}}}                                                                                                                                                                                                   \\
  \hline
  \multicolumn{{6}}{{|p{{15cm}}|}}{{\textbf{{ {more_info} }}}}                                                                                                                                                                                                                                                            \\
  \hline
  \multicolumn{{6}}{{|l|}}{{\cellcolor{{hexingblue}}{{\color{{white}} \textbf{{Foto - Posição de instalação do {host} }}}}}}                                                                                                                                                                                             \\
  \hline
  \multicolumn{{6}}{{|c|}}{{%
    \begin{{minipage}}{{\dimexpr\textwidth-2\tabcolsep-2\arrayrulewidth\relax}}
      \setlength{{\parindent}}{{0pt}}%
      \begin{{minipage}}[t]{{0.48\textwidth}}
        \raisebox{{-1\height}}{{%
          \setlength{{\fboxsep}}{{2mm}}%
          \setlength{{\fboxrule}}{{0pt}}%
          \fbox{{\includegraphics[width=\linewidth, scale=2, height=14cm,keepaspectratio]{{ {temp_image1} }}}}%
        }}
      \end{{minipage}}\hfill
      \begin{{minipage}}[t]{{0.48\textwidth}}
        \raisebox{{-1\height}}{{%
          \setlength{{\fboxsep}}{{2mm}}%
          \setlength{{\fboxrule}}{{0pt}}%
          \fbox{{\includegraphics[width=\linewidth,height=6.9cm,keepaspectratio]{{ {temp_image2} }}}}%
        }}\\[1mm] % Small vertical space between images
        \raisebox{{-1\height}}{{%
          \setlength{{\fboxsep}}{{2mm}}%
          \setlength{{\fboxrule}}{{0pt}}%
          \fbox{{\includegraphics[width=\linewidth,height=6.9cm,keepaspectratio]{{ {temp_image3} }}}}%
        }}
      \end{{minipage}}
    \end{{minipage}}%
  }}                                                                                                                                                                                                                                                                                                     \\
  \hline
\end{{tabularx}}
\end{{document}}
"""
