"""
Copyright (C) 2023 TH Köln – University of Applied Sciences

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
import string

from GraphModel.Graph import Graph
from GraphModel.Node import Node


class GraphContent:
    nodeList = []  # List of all Nodes

    # Requirement
    # 20 Nodes per Member
    # 30.000 Words per Member
    # ~~=> 1500 Words per node

    # Demands to group
    # 3 x 20 nodes     = 60 nodes
    # 3 x 30.000 words = 90.000 words

    def __init__(self, graph: Graph):
        self.NodeGraphCreateFromTeamDeez(graph)
        #self.create_demo_nodes(graph)

    def NodeGraphCreateProgrammingTree(self, parrant : Node):
        node = Node("No", "Programming")
        self.nodeList.append(node)
        node.connect(parrant)

        nodeDataFormat = self.NodeGraphCreateSubTree(
            "Dateiformat",
            "Dateien werden in unterschiedlich Formaten gespeichert, je nach dem wie man diese nutzen möchte."
            "Hier sind entweder **Text** vasiert oder auch **Binär**. Beide mit ihren vor und nachteilen.\n"
            "Zusätzlich gibt es auch gemischte formate, "
            "da das lesen und schreiben dieser Formate aber ehr unkomfortabel ist, wird die nutzung ehr vermieden",
            node)
        nodeBinary = self.NodeGraphCreateSubTree(
            "Binary",
            "Das Binär format ist effizient in der speicherung, "
             "## Vorteile\n"
            "- Einfacher zu lesen und zu schreiben als Text basierte Dateien\n"
            "## Nachteile\n"
            "- Ist nicht direkt änderbar, man benötigt ein Programm um die Datei zu verändern.\n"
            "- Sollte man diese Fehlerhaft abändern, kann es dazu kommen, das die Datei nicht mehr lese fähig wird.",
            nodeDataFormat)
        self.NodeGraphCreateSubTree(
            "AAC",
            "# Advanced Audio Coding\n"
            "## [ISO/IEC 14496-3:2019]\n"
            "Soundformat, nachfolger von MP3",
            nodeBinary)

        self.NodeGraphCreateSubTree(
            "AVI",
            "# Audio Video Interleave\n"
            "## [RFC 2361]\n"
            "Video format, unkompremiert.\n"
            "Da dieses Format keine kompression besitzt, werden Dateien mit mehr Inhalt in größe explodieren"
            "Due ",
            nodeBinary)
        self.NodeGraphCreateSubTree(
            "BMP",
            "# BitMap\n"
            "# [RFC 797]\n"
            "Bild format, unkompremiert.\n"
            "## Vorteile\n"
            "- Einfach zu lesen und auch zu schreiben\n"
            "## Nachteile\n"
            "- Durch fehlende kompresssion werden Bilder mit viel Detail enorm groß.\n"
            "- Transparenz ist zwar möglich aber oft nicht unterstützt."
            "## Links\n",
            nodeBinary)
        self.NodeGraphCreateSubTree(
            "FLAC",
            "# Free Lossless Audio Codec\n"
            "## Info\n"
            "Öffenticher standard\n"
            "### Abhänigkeiten\n"
            "- CRC\n"
            "### Vorteile\n"
            " - Erhöhte Kompression als DELFATE durch bessere Nutzung der Eigenschaften von Audio Dateien."
            "### Nachteile\n"
            "- (Keine)"
            "## Links\n",
            nodeBinary)
        self.NodeGraphCreateSubTree(
            "FBX",
            "# Kaydara Film Box\n"
            "### Abhänigkeiten\n"
            "- ZLIB"
            "### Vorteile\n"
            "### Nachteile\n"
            "- Schwierig zu lesen und schreiben\n"
            "## Links\n",
            nodeBinary)
        self.NodeGraphCreateSubTree(
            "GIF",
            "# Graphics Interchange Format\n"
            "## Info\n"
            "### Abhänigkeiten\n"
            "### Vorteile\n"         
            "### Nachteile\n"
            "## Links\n"
            "- Wikipedia : https://en.wikipedia.org/wiki/GIF",
            nodeBinary)
        self.NodeGraphCreateSubTree(
            "MIDI",
            "# Musical Instrument Digital Interface\n"
            "Ein sehr bekanntes Musik format aus den 1980s.\n"
            "In diesem werden Instrumente und deren Noten abgespeichert."
            "Wie diese sich aber genau anhören ist der Soundkarte überlassen"
            "Da nur die Noten gespeichert werden, ist dieses Format sehr speicher effizient."
           "## Links\n"
            "- Wikipedia : https://en.wikipedia.org/wiki/MIDI\n",
            nodeBinary)
        self.NodeGraphCreateSubTree(
            "MP3",
            "# Moving Picture Experts Group Layer III\n"
            "## Info\n"
            "### Abhänigkeiten\n"
            "- ID3\n"
            "### Vorteile\n"         
            "### Nachteile\n"
            "## Links\n",
            nodeBinary)
        self.NodeGraphCreateSubTree(
            "MTL",
            "# Wavefront Material Template Library\n"
            "## Info\n"
            "### Abhänigkeiten\n"
            "- (Keine)\n"
            "### Vorteile\n"         
            "### Nachteile\n"
            "## Links\n",
            nodeBinary)
        self.NodeGraphCreateSubTree(
            "OBJ",
            "# Wavefront\n"
            "## Info\n"
            "### Abhänigkeiten\n"
            "- MTL\n"
            "### Vorteile\n"         
            "### Nachteile\n"
            "## Links\n",
            nodeBinary)
        self.NodeGraphCreateSubTree(
            "OGG",
            "# xxxxxxxxxxx\n"
            "## Info\n"
            "### Abhänigkeiten\n"
            "### Vorteile\n"         
            "### Nachteile\n"
            "## Links\n",
            nodeBinary)
        self.NodeGraphCreateSubTree(
            "PDF",
            "# Portable Document Format\n"
            "# [ISO 32000]\n"
            "## Info\n"
            "### Abhänigkeiten\n"
            "### Vorteile\n"
            "### Nachteile\n"
            "## Links\n",
            nodeBinary)
        nodePNG = self.NodeGraphCreateSubTree(
            "PNG",
            "# Portable Network Graphics\n"
            "# [RFC 2083]\n"
            "## Info\n"
            "### Abhänigkeiten\n"
            "### Vorteile\n"
            "### Nachteile\n"
            "## Links\n",
            nodeBinary)
        self.NodeGraphCreateSubTree(
            "JPG",
            "# Joint Photographic Experts Group\n"
            "# [ISO/IEC 10918]\n"
            "# xxxxxxxxxxx\n"
            "## Info\n"
            "### Abhänigkeiten\n"
            "### Vorteile\n"
            "### Nachteile\n"
            "## Links\n",
            nodeBinary)
        self.NodeGraphCreateSubTree(
            "TGA",
            "Truevision Advanced Raster Graphics Array\n"
            "## Info\n"
            "### Abhänigkeiten\n"
            "### Vorteile\n"
            "### Nachteile\n"
            "## Links\n",
            nodeBinary)
        self.NodeGraphCreateSubTree(
            "STL",
            "# Standard Triangle Language\n"
            "# xxxxxxxxxxx\n"
            "## Info\n"
            "### Abhänigkeiten\n"
            "### Vorteile\n"
            "### Nachteile\n"
            "## Links\n",
            nodeBinary)
        self.NodeGraphCreateSubTree(
            "SVG",
            "# Scalable Vector Graphics\n"
            "# xxxxxxxxxxx\n"
            "## Info\n"
            "### Abhänigkeiten\n"
            "### Vorteile\n"
            "### Nachteile\n"
            "## Links\n",
            nodeBinary)
        self.NodeGraphCreateSubTree(
            "TIFF",
            "# Tagged Image File Format\n"
            "## Info\n"
            "### Abhänigkeiten\n"
            "### Vorteile\n"
            "### Nachteile\n"
            "## Links\n",
            nodeBinary)
        self.NodeGraphCreateSubTree(
            "TTF",
            "# True Type Font\n"
            "## Info\n"
            "### Abhänigkeiten\n"
             "- (Keine)\n"
            "### Vorteile\n"
            "### Nachteile\n"
            "## Links\n",
            nodeBinary)
        self.NodeGraphCreateSubTree(
            "WAV",
            "# Wave\n"
            "## Info\n"
            "### Abhänigkeiten\n"
            "- (Keine)\n"
            "### Vorteile\n"
            "### Nachteile\n"
            "## Links\n",
            nodeBinary)

        nodeText = self.NodeGraphCreateSubTree(
            "Text",
            "# Text basierte Dateien\n"
            "## Info\n"
            "### Abhänigkeiten\n"
            "- Text Editor\n"
            "### Vorteile\n"
            "- Menschlich einfaches lesen und schreiben\n"
            "### Nachteile\n"
            "- Benötig ein Komplexes Kompilier system um die Datei in "
            "verarbeitbare daten zu konvertieren\n"
            "## Links\n",
            nodeDataFormat)
        self.NodeGraphCreateSubTree(
            "JSON",
            "# JavaScript Object Notation\n"
            "## Info\n"
            "### Abhänigkeiten\n"
            "- (Keine)\n"
            "### Vorteile\n"
            "### Nachteile\n"
            "## Links\n",
            nodeText)
        self.NodeGraphCreateSubTree(
            "YAML",
            "# Wave\n"
            "## Info\n"
            "### Abhänigkeiten\n"
            "- (Keine)\n"
            "### Vorteile\n"
            "### Nachteile\n"
            "## Links\n",
            nodeText)
        self.NodeGraphCreateSubTree(
            "XML",
            "# Wave\n"
            "## Info\n"
            "### Abhänigkeiten\n"
            "- (Keine)\n"
            "### Vorteile\n"
            "### Nachteile\n"
            "## Links\n",
            nodeText)
        self.NodeGraphCreateSubTree(
            "INI",
            "# Wave\n"
            "## Info\n"
            "### Abhänigkeiten\n"
            "- (Keine)\n"
            "### Vorteile\n"
            "### Nachteile\n"
            "## Links\n",
            nodeText)

        nodeLanguage = self.NodeGraphCreateSubTree(
            "Languages",
            "", node)
        nodeMachineLanguage = self.NodeGraphCreateSubTree(
            "Machine Language",
            "",
            nodeLanguage)
        self.NodeGraphCreateSubTree(
            "x86",
            "",
            nodeMachineLanguage)
        self.NodeGraphCreateSubTree(
            "ARM",
            "",
            nodeMachineLanguage)
        self.NodeGraphCreateSubTree(
            "MIPS",
            "",
            nodeMachineLanguage)

        nodeDataOriented = self.NodeGraphCreateSubTree(
            "Data Oriented",
            "", nodeLanguage)
        self.NodeGraphCreateSubTree(
            "C",
            "",
            nodeDataOriented)
        nodeCPP = self.NodeGraphCreateSubTree(
            "C++",
            "",
            nodeDataOriented)

        nodeObjectOriented = self.NodeGraphCreateSubTree(
            "Object Oriented",
            "",
            nodeLanguage)
        self.NodeGraphCreateSubTree(
            "Java",
            "",
            nodeObjectOriented)
        self.NodeGraphCreateSubTree(
            "C#",
            "",
            nodeObjectOriented)
        self.NodeGraphCreateSubTree(
            "VB.Net",
            "",
            nodeObjectOriented)

        nodeCPP.connect(nodeObjectOriented)

        nodeFunctional = self.NodeGraphCreateSubTree(
            "Functional",
            "# Funktionale Sprachen",
            nodeLanguage)
        self.NodeGraphCreateSubTree(
            "Haskell",
            "",
            nodeFunctional)

        nodeScript = self.NodeGraphCreateSubTree(
            "Script",
            "# Skript Sprachen",
            nodeLanguage)
        self.NodeGraphCreateSubTree(
            "Bash",
            "",
            nodeScript)
        self.NodeGraphCreateSubTree(
            "PowerShell",
            "",
            nodeScript)
        self.NodeGraphCreateSubTree(
            "CMD",
            "# Windows Commandline\n"
            "Die Windows Commandline ist, wie man sie auch schon seit DOS kennt, die bekannte Schwarze Konsole.",
            nodeScript)
        self.NodeGraphCreateSubTree(
            "VBS",
            "# Visual Basic Script\n"
            "Dies ist eine Script Form von VisualBasic.NET. Dies wird meist in Excel als Makro funktionen genutzt",
            nodeScript)

        nodeRelational = self.NodeGraphCreateSubTree(
            "Relational",
            "# Relationale Sprachen\n"
            "Relationale Sprachen arbeiten, anders als bekannte iterative Sprachen, mit Mengen an Daten.\n"
            "",
            nodeLanguage)
        self.NodeGraphCreateSubTree(
            "SQL",
            "# Structured query language\n"
            "SQL ist die standardsprache wenn es um Datenbanken geht.\n"
            "",
            nodeRelational)
        self.NodeGraphCreateSubTree(
            "Prolog",
            "",
            nodeRelational)

       # nodeHardware = self.NodeGraphCreateSubTree("Hardware", "", node)
        nodeMemory = self.NodeGraphCreateSubTree(
            "Memory",
            "# Speicherverwaltung\n"
             "## Info\n"
            "Die "
            "### Abhänigkeiten\n"
            "- BetriebSystem\n"
            "### Vorteile\n"
            "Durch das manuelle verwalten kann Code Qualität erhöht werden und dessen geschwindigkeit "
            "stark verbessert werden.\n"
            "### Nachteile\n"
            "Manuelle Speicherverwaltung ist nicht unbedingt einfach, viele Programmierer behaupten auch, "
            "dass dies eineer der schwersten Themen ist. Die Schwiereigkeit besteht im größeren nur "
            "gegebenen speicher wieder frei zu geben. "
            "## Links\n",
            node)
        self.NodeGraphCreateSubTree(
            "Garbage Collector",
            "# Der Speicherverwalter\n"
            "In den meisten Programmiersprachen werden alle dynamischen elemente von "
            "einem Speicher-Verwaltungssystem verarbeitet. Dadurch ist es nicht mehr "
            "notwendig manuell Speicher an zu vordern und auch wieder frei zu geben\n\n"
            "Als großer Nachteil kommt immer wieder die kosten von Speicher und "
            "Geschwinigkeit zum Vordergrund."
            "Hier ist genau der verwaltungsaspekt einer der größten probleme. "
            "Nicht unbedingt die umsetzuing aber das verhalten der verwaltung der Elemente."
            "Oftmals werden Probleme erst wahrgenommen und erkannt wenn es schon zu spät ist\n\n",
            nodeMemory)
        self.NodeGraphCreateSubTree(
            "Stack",
            "# Speicher Stapel\n"
             "## Info\n"
            "Der Stapel ist einer der ersten Speicher-Systeme die man kennen lernt, da diese "
            "einer der einfachen sind. Dieser arbeitet mit dem First-In-Last-Out (FILO) Prinzip\n\n"
            "### Abhänigkeiten\n"
            "- BetriebSystem\n"
            "### Vorteile\n"
            "- Extrem Schnelles Hinzufügen und Entfernen von Daten\n"
            "### Nachteile\n"
            "- Daten die zuerst hinzugefügt werden leben immer länger als Elemente die auf diesem liegen\n"
            "- Der Speicher ist begrenzt und zu große oder auch zu viele Elemente können einen Fehler erzeigen.",
            nodeMemory)
        self.NodeGraphCreateSubTree(
            "Heap",
            "# Speicher Haufen\n"
            "Der Weg um dynamisch außerhalb des Stacks Speicher an zu fordern."
            "Da der Speicher außerhalb liegt, wirkt der sich der Heap auch nicht auf den Stack aus."
            "Jedoch ist es möglich, das durch das aufblähen des Heaps und des Stacks zugleich eine kollision entsteht",
            nodeMemory)
        self.NodeGraphCreateSubTree(
            "Mapping",
            "# Speicher Abbilden\n"
            "Mapping ist anders zu den anderen Speicher Arten rellativ neu.\n"
            "Ähnlich wie der Heap existiert diese Art Speicher nicht im Stack sondern in einem Seperaten Bereich\n\n"
            "Dieser Bereich ermöglicht es einen gewissen Block fest in den Virtuellen Speicher Bereich ein zu arbeiten."
            "### Abhänigkeiten\n"
            "- Virtueller Speicher",
            nodeMemory)

        nodeAlgoritm = self.NodeGraphCreateSubTree("Algorithms", "", node)
        nodeLZ77 = self.NodeGraphCreateSubTree("LZ77", "", nodeAlgoritm)
        nodeZLIB = self.NodeGraphCreateSubTree(
            "ZLIB",
            "ZLIB ist eine Struktur die Kompessions-Algorithmen unterstützt.\n"
            "Zurzeit ist nur DEFLATE definiert.\n",
            nodeAlgoritm)
        nodeADLER = self.NodeGraphCreateSubTree(
            "ADLER",
            "Ein Überprüfsummen Algorithmus der einen block Daten überpüfen kann",
            nodeAlgoritm)
        nodeCRC = self.NodeGraphCreateSubTree(
            "CRC",
            "# Cyclic redundancy check",
            nodeAlgoritm)
        nodeADAM7 = self.NodeGraphCreateSubTree(
            "ADAM7",
            "Ein Interlacing Algorithmus der durch "
            "[Interlacing](https://en.wikipedia.org/wiki/Interlacing_(bitmaps))"
            "[Wikipedia](https://en.wikipedia.org/wiki/Adam7_algorithm)",
            nodeAlgoritm)
        nodeDELFATE = self.NodeGraphCreateSubTree(
            "DEFLATE",
            "Ein Kompessions Algorithmus der von ZLIB genutzt wird.\n"
            "Dieses format nutzt zusätzlich den Huffman Algorithmus\n"
            "Dadurch ist dieses Format zwar von sich aus limitiert auf byte Ebene aber der Inhalt ist auf bit Ebene.",
            nodeAlgoritm)
        nodeHuffman = self.NodeGraphCreateSubTree(
            "Huffman",
            "Ein Kompessions Algorithmus der auf bit Ebene funktioniert.",
            nodeAlgoritm)

        nodePNG.connect(nodeZLIB)
        nodePNG.connect(nodeADAM7)
        nodePNG.connect(nodeCRC)
        nodeZLIB.connect(nodeDELFATE)
        nodeZLIB.connect(nodeADLER)
        nodeDELFATE.connect(nodeHuffman)
        nodeDELFATE.connect(nodeLZ77)

        nodePattern = self.NodeGraphCreateSubTree(
            "Entwurfsmuster",
            "## Info\n"
            "Auch Design-Patterns genannt, sind wiederkehrende Lösungen die als Vorlage dienen."
            "IN der Programmierung werden Probleme oft auf eine gleiche Art gelößt, "
            "hier lohnt es sich mit diesen Vorlagen schon bekannt zu sein um nicht "
            "sehr viel Zeit und Mühe zu verbrauchen."      
            "### Abhänigkeiten\n"
            "- (Keine)\n"
            "### Vorteile\n"
            "- Code ist mehr Standartisiert mit weniger halben Mustern.\n"
            "- Erleichterte Entwicklung durch Grundwissen\n"
            "- Erprobte Muster können die Code Qualität erhöhen\n"
            "### Nachteile\n"
            "- Erzwingung dieser Muster kann sich stark negativ auf die Qualität des Codes auswirkien.\n"
            "- Muster zu nutzen verändert den Code, acht ist zu geben das es nicht zu stark verzerrt.\n"
            "- Falsche Anwenung der Muster kann ungeahnte Probleme mit sich ziehen.\n"
            "## Links\n",
            node)
        self.NodeGraphCreateSubTree(
            "State Machine",
            "# Zustandsmachine"
            "## Info\n"
            "Die Zustandsmachine existiert immer in einem Fest definierten "
            "Zustand und kann diesen nur in fest eingebauten Wegen ändern."
            "Dieses Muster wird oft in kleinen Abgeschlossenen system verwendet."
            "Als Beispiel kleine Automaten, für Getränke oder andere Produkte "
            "aber auch kleine MicroChips oder auch kleine Elemente in Spielen."
            "### Abhänigkeiten\n"
            "- Ein Wert der den Momentanen Status hält\n"
            "- Eine Liste von allen möglichen Zuständen\n"
            "### Vorteile\n"
            "- Exakte definition vom jetzigen Zustand\n"
            "- Vehinderung von Illegalen Zuständen\n"
            "### Nachteile\n"
            "- Nur einzelne Zustände möglich\n"
            "- Parraleles Arbeiten unmöglich.\n"
            "## Links\n",
            nodePattern)
        self.NodeGraphCreateSubTree(
            "Observer",
            "# Observierungs Muster\n"
            "## Info\n"
            "### Abhänigkeiten\n"
            "- Sender\n"
            "- Empfänger\n"
            "### Vorteile\n"
            "- Schnelle direkte Event basierte Aktionen\n"
            "### Nachteile\n"
            "- Die Empfänger können den Aufruf aufhalten, wenn dieser syncron genutzt wird."
            "## Links\n",
            nodePattern)
        self.NodeGraphCreateSubTree(
            "Owner",
            "## Besitzer Muster\n"
            "## Info\n"
            "Dieses Muster dient dazu, das nur der Besitzer einem gewissen Elements kontrolle hat dieses zu verändern\n"
            "Durch diese stränge KOntrolle wird verhindert das drtitte veränderungen treffen können, "
            "die dafür sorgen können das ein illegaler zustand entsteht."
            "### Abhänigkeiten\n"
            "- Besitzer\n"
            "### Vorteile\n"
            "- Schnelle direkte Event basierte Aktionen\n"
            "### Nachteile\n"
            "- Die Empfänger können den Aufruf aufhalten, wenn dieser syncron genutzt wird."
            "## Links\n",
            nodePattern)

        nodeProtocol = self.NodeGraphCreateSubTree(
            "Protocol",
            "Ein Protokoll dient zur Definition der Kommunikation zwischen Systemen."
            "Diese sind essenziell, da ohne sie Kommunikation nicht nur probleme bereitet sondern gar fehlerlos unmöglich ist.\n\n"
            "Um nun also dieses Problem zu lösen, wird lange an einem Protokoll entwickelt "
            "und getestet um möglichst alles ab zu decken was man unter diesen Aspekten benötig."
            "Zudem wird eine Dokumentation erstellt die alle Interaktionen und Fragen abdecken "
            "muss um zukünfigte auftretende Fragen des Nutzers direkt eine Antwort zu bieten\n\n"
            "# Limitierungen\n"
            "Auftretende Probleme sind immer wieder, das bestimmte erwünste Aktionen nur umständlich"
            " oder sogar gar nicht möglich sind. In vielen anderen Situationen gibt es auch Probleme, "
            "dass gewisse Interaktionen nicht definiert und somit unerwünscht sind.\n\n"
            "Um damit um zu gehen muss im gegebenen Fall vorab damit gerechnet werden und mögliche "
            "Stellen zum einfügen von Erweiterungen gedacht werden.\n"
            "Hier wird sehr oft auf die simple **Versions ID** genutzt. <Hier kann schnell unterschieden werden "
            "welche kommunikations version genutzt wird. Entweder kann die version unterstützt werden aber auch abgelehnt werden.",
            node)
        self.NodeGraphCreateSubTree(
            "LDAP",
            "# Lightweight Directory Access Protocol\n"
            "# [RFC 1823]\n"
            "# [RFC 4515]\n"
            "## Info\n"
            "Ein Verzeichnis service der es auch extram hardwarearmen system ermöglicht größere Datenmängen zu verwalten"
            "### Abhänigkeiten\n"
            "- Mindestens 2 Aktöre, Server und Client\n"
            "### Vorteile\n"
            "- Unterstützt von sehr vielen Systemen und Anwendungen\n"
            "### Nachteile\n"
            "- Limitierte Funktionen\n"
            "- Verbindungslose varriante ist offitiell nicht mehr erwünscht\n"
            "## Links\n"
            "- Wikipedia : https://de.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol",
            nodeProtocol)
        self.NodeGraphCreateSubTree(
            "FTP",
            "# [RFC 959]\n"
            "## Info\n"
            "# File Transfer Protocol"
            "Ein Netzwerk Protokoll um über TCP/IP zu kommunizieren.\n"
            "Als Kernfunktion ist der Datenaustausch zwischen einem Client und einem Server.\n"
            "Dieses Protokoll wird oft genutzt um Daten zwischen Client und Server zu verschieben\n"
            "### Abhänigkeiten\n"
            "- Mindestens 2 Aktöre, Server und Client\n"
            "### Vorteile\n"
            "- Unterstützt von sehr vielen Systemen und Anwendungen\n"
            "### Nachteile\n"
            "- Limitierte Funktionen\n"
            "- Verbindungslose varriante ist offitiell nicht mehr erwünscht\n"
            "## Links\n",
            nodeProtocol)


    def NodeGraphCreateAAAAAAATree(self, parrant: Node):
        node = Node("No", "PPP")
        self.nodeList.append(node)
        node.connect(parrant)
    def NodeGraphCreateOrganisationTree(self, parrant: Node):
        node = Node("No", "Organisation der Universitäten")
        self.nodeList.append(node)
        node.connect(parrant)

        nodeKurse = self.NodeGraphCreateSubTree("Kurse",
                                                "Manche Kurse sind Pflicht, während andere wählbar sind. Die Menge der Wählbaren Kurse anderer Studiengänge"
                                                " ist jedoch sehr Klein und stark Begrentzt. Eine bessere Konfigurierung des Studiums wie im Master ist stark wünschenswert."
                                                "Die Meinung aus dem Vorigen Satzt war mit eine der meist getätigten Aussagen von Studenten im Studiengang Allgemeine Informatik."
                                                "Zudem ist die Errechnung der Bearbeitungsdauer/ETC-Punkte teilweise sehr Unstimmig. Ein sher gutes Beispiel zu diesem Punkt" 
                                                " ist die Bachelorarbeit welche 12 ETC-Punkte gibt und die einarbeitung in diese selten kürzer ist als die veranschlagte Zeit"
                                                " für die Bachelorarbeit und zwar 360 Stunden."
                                                , node)

        nodeBachelorarbeit = self.NodeGraphCreateSubTree("Bachelorarbeit",
                                                         "Eine Bachelorarbeit wird meist als Ende des Bachelorstudiums gesehen jedoch stimmt dies nicht wirklich. Diese kann normalerweise"
                                                         " ab Sammlung der hälfte der zum Abschluss benötgen ETC-Punkte beantragt werden (Referenziert von einem Studenten der Uni Siegen)."
                                                         "Die Bewertung der Bachelorarbeit mit 12 ETC-Punkten ist von einigen Studenten fraglich unter der bedingung dass ein ETC-Punkt 30 Stunden Arbeit entsprechen."
                                                         "Aus berrichten anderer Studenten von dieser und von anderen Universitäten sind diese 360 Stunden als minimum zum Schreiben und Formulieren der Bachelorarbeit zu verplanen."
                                                         "Durch diesen Unterschied wird von Studenten oftmals die Bearbeitund der Bachelorarbeit erst Beantragt wenn diese schon Fertig durchgeführt und geschrieben ist um nicht"
                                                         " den 9 oder 12 Wochen bearbeitungszeitraum zu überschreiten."
                                                         , node)

        nodeDruck = self.NodeGraphCreateSubTree("Zeitdruck der Bachelorarbeit",
                                                "Da die Bachelorarbeit ab anmeldung ein Zeitlimit von 9 oder 12 Wochen hat entsteht Zeitdruck ob man dies Überhaupt in dieser Zeit schafft. Viele Studenten starten ihre"
                                                " Bachelorarbeit erst, wenn diese Vollständig beendet ist. Aus Quelllen anderer Studenten die am Master Sitzen oder Ihr Studium mit der Bachelorarbeit beendet haben, habe ich auch"
                                                " auch von einem Fall erfahren wo jemand an 9 Monate an seiner Bachelorarbeit saß."
                                                , nodeBachelorarbeit)

        nodeBachelorarbeitBeiFirmen = self.NodeGraphCreateSubTree("Bachelorarbeit in einem Konzern",
                                                                  "Es wirkt Profitabel seine Bachelorarbeit einem Konzern zu schreiben, da man denkt es sei ja schön für die Bearbeitung seiner Bachelorarbeit bezahlt zu werden."
                                                                  "Das große Problem in dem ich bin ist, dass ich durch das beheben eines Problems und das Längere einlesen in die Thematik gelernt habe dass dies nicht wirklich von Personen"
                                                                  " Verwendet wird und durch die kleine Lösung des Existiernden Problems auch für den Konzern aus meiner Sicht und deswegen Schuldgefühle wegen der Verschwendung meines Gehlats"
                                                                  " sich bilden."
                                                                  , nodeBachelorarbeit)

        nodeInformationensfluss = self.NodeGraphCreateSubTree("Quellen für Informationen",
                                                              "Um einwenig zu Visualisieren wie viele verschiedene Quellen für Informationen es gibt die alle genutzt werden nutze ich diesen Knote."
                                                                        "Die Bewertung der verschiedenen Informationsquellen hängt von dem verhältnis von Qualität und Quantität der Medien und des aufwands diese Informationen zu erhalten."
                                                              ,node)
        nodeEmails = self.NodeGraphCreateSubTree("E-Mails",
                                                 "Der Kontakt per E-Mail ist zwar wegen der Präsentz durch zum Beispiel Weiterleitug sehr Gut. Ein Kritik Punkt ist, jedoch die Nachrichten überflutung."
                                                 "Die Präsentz wird jedoch nur so hoch gewertet da Kommulitonen berrichten ihre E-Mails auf dem Handy zu haben und somit nicht den Aufwend habe Täglich Nachrichten zuüberprüfen obwohl teilweise keine neuen infos da sind."
                                                 "Den Informations überfluss ist auch anscheinend Groß für die Professoren. Diese Annahme resultiert aus mehreren Kommunikationen mit Professoren die Nachrichten die sie betreffen nur durch die Hohe Priorität"
                                                 " von den allgemeinen Informationen von einem anderen Kampus nur dürch die Priorität unterscheiden können."
                                                  , nodeInformationensfluss)

        nodeILIAS = self.NodeGraphCreateSubTree("ILIAS/ILU",
                                                "Das Illias ist das Alte System um alle Dateien zu bündlen. Informationen von diesem System, werden glücklicherweise per E-Mail weitergeleitet, jedoch wird das Hochladenm von dateien nur gemeldet wenn es in einer Gruppe ist."
                                                "Illias ist jedoch wenn die Daten gut Sortiert wurden die Zweit/Dritt beste Datenquelle da nur Modul relevantes in den Kursen sind. Dies wird auch Teilweise zur abgabe von Praktika genutzt um nicht unfaire vorteile Studenten zu geben"
                                                " die einen Späteren kontroll Termin haben. Das Ilias hat auch ein Forum für Generelle frage zur Vorlesung und Organisation welches jedoch nur im äußersten genutzt wird da generellere Fragen meist in den Vorlesungen geklärt werden."
                                                , nodeInformationensfluss)

        nodeTHeLearning = self.NodeGraphCreateSubTree("THe-learning",
                                                       "THe-learning ist die beste Lernplatform der TH-Köln laut einiger Kommulitonen. Ein besonders guter Vorteil ist die Fortschrittleiste da für die Kurse es eine Gute Rückmeldung gibt wie weit man im vergleich zu den Erwartungen"
                                                        " des Professors ist. Zudem fördert diese Lernplatform Vorlesungen zusammengefasst hochzuladen um trotzdem auf Frage von Studenten einzugehen zu können hat jede Übung und Vorlesung ein Kommentarbereich. Auf dieser Platform sind"
                                                        " die Vorlesungen und Übungen Chronologisch nach abfolg wie diese Themen zu lernen sind. Um Fragen und Kommentare aller Art zu fördern werden die Steller Anonymisiert."
                                                       , nodeInformationensfluss)

        nodeWhatsappChats = self.NodeGraphCreateSubTree("Whatsapp Gruppen",
                                                        "Whatsapp Gruppen von Kursen werden oft von Studenten selber erstellt. Teils werden auf diese Whatsapp Gruppen in den Vorlesungen kurz hingewiesen. Diese Gruppen haben die beste Möglichkeit um generelle Wissens fragen ohne"
                                                        " individuell den Professor zu Kontaktieren. Ein riesen Nachteil ist jedoch, dass nicht immer eine Antwort garantiert ist."
                                                        ,nodeInformationensfluss)

        nodeTHKoelnWebseite = self.NodeGraphCreateSubTree("Die TH Köln Webseite",
                                                          "Die Webseite der TH Köln ist sehr unübersichtlich und schwer zu Navigieren der einzige Weg Informationen aus der Webseite zu bekommen iost durch Google."
                                                          , nodeInformationensfluss)

        nodeStudienBuero =self.NodeGraphCreateSubTree("Studienbüro",
                                                      "Das Studienbüro soll als Anlaufstelle für Fragen zur Organisierung des Studiums. Jedoch wurde mir geschildert von einem Mentor, dass Studenten es meiden da dass Personal dort sehr angespannt sei bei rückfragen"
                                                      , nodeInformationensfluss)

        nodePraktika = self.NodeGraphCreateSubTree("Praktika",
                                                   "Das vollenden der Praktika ist zur Prüfungs-anmeldung der Kurse Notwendig. Manche Praktika erfordern Gruppenarbeit jedoch kann dies schädlich sein, da Gruppen Mitglieder die Leistung anderer zu dem machen müssen und Endprojekte"
                                                   " ohne Pflicht Meilensteine die Bearbeitung Flexiebeler macht und so anpassbarer an Persönliche Lagen macht. Manche Kurse erlauben eine anerkennung für das Praktikum  wenn eine Ausbildung in dem Berreich des Moduls absolviert wurde."
                                                   , nodeInformationensfluss)

        nodeÜbergreifendeModule = self.NodeGraphCreateSubTree("Studiengang Übergreifende Module",
                                                              "Studiengang Übergreifende Module sind in den ersten 2 Semestern sehr hilfreich da so Theorethisch ein Grundverständniss der Themen sichergestellt sein sollte. In der Praxis habe ich festgestellt dass Kurse die als nicht so"
                                                              " wichtig gesehen werden nur zwangsweise gelernt werden, jedoch wieder schnell vergessen werden (Ein beispiel ist Algorithmik und Programmierung für Wirtschafts-Informatiker). Zu dem führen diese Kurse leider dazu Tendieren die geringste"
                                                              " gemeinsamkeit zu lehren was dann in folge Kursen Kompensiert werden muss."
                                                              , nodeKurse)

        nodePrüfung = self.NodeGraphCreateSubTree("Prüfung",
                                                  "Prüfungen können verschiedenst ausfallen wie in diesem Modul baut sich die Note aus den einzelnen Praktika gepaart mit dem Abschluss Projekt zusammen. Andere Module haben Prüfungen in Müdlicher Form. Die Beste Form der Prüfung meiner Meinung"
                                                  " nach ist, jedoch die Projekt Prüfung. Dies art der Prüfung ist, jedoch nur gut wenn dieses Projekt auch die Praktika ablöst. Das Kritischste Problem was Studenten sehen was nur in den Modulen ST1, ST2 und AP1 vernümpftig umgesetzt wurde, war Aufgaben in denen mann Code"
                                                  " Schreiben muss. Diese Fragen haben das Problem dass diese mit Code Editoren geschreiben werden sollten und meist zu knapp abgemessen wurden. Wegen dieser Fragen konnte ich AP2, welches ich im Sommersemester 2020 belegt habe nur durch eine bewertete Ausarbeitung"
                                                  " bestehen. Dies wird leider nicht mehr angeboten da es zu viel aufwand zur überprüfung ist, dies ist Schade da diese Art der Prüfung bei Studenten Sehr beliebt sind."

                                                  ,nodeKurse)

        nodeBesondereUmstände = self.NodeGraphCreateSubTree("Besondere Umstände im Studium",
                                                            "Es gibt mehrere Besondere Umstände im Studium die das Studium Erschweren können."
                                                            ,node)

        nodeStudiumBeiEltern = self.NodeGraphCreateSubTree("Leben bei den Eltern",
                                                           "Das Studium im Elternhaus kann Kostenspaarend sein wobei, jedoch selbst bei nicht Aktivem Druck durch die Eltern das Studium so schnell wie möglichst zu Beenden dieser auftritt. Dieses Problem kann sich auch mit anderen Problemen"
                                                           " kombinieren wie zum Beispiel dem Problem des Arbeitens währen des Studium. Dies kann bei Studierenden teilweise auch ein Drang sein da die Familie dieses Geld benötigt."
                                                           , nodeBesondereUmstände)

        nodeStudierenInRegelstudienzeit = self.NodeGraphCreateSubTree("Studium in Regelstudienzeit",
                                                                      "Das Studium in Regelstudienzeit ist im normal Fall unmöglich. Um in der Regelstudienzeit zu bleiben darf kein Fehler Passieren und wie schon benannt im Punkt Praktikum dass man aufgrund der Gruppe dieses Praktikum nicht besteht."
                                                                      "Dies führt dazu dass man Aufgrund der Praktika und der Prüfungen keine Pausen hat und sehr viel Stress."
                                                                      , nodeBesondereUmstände)

        nodeStudiumMitADHS = self.NodeGraphCreateSubTree("Studium mit ADHS",
                                                         "ADHS ist eine starke Erschwerung für das Studium da Studenten mit ADHS geschildert haben öfters beim wiederholen von Punkten oder weiteremerläutern leicht abschweife bei den Vorlesungen. Dieses Abschweifen brachte sie dazu manche Themen zu verpassen welche sie nur durch"
                                                         " das erfragen von Kommulitonen lernen konnten. Aus diesem Grund bevorzugen sie die Vorlesungern im THe-Learning da diese Themen kurz auf den Punkt bringen und für sie das selber Recherchieren fördert. Einer dieser Studenten habe bisher einen Nachteilsausgleich nur für ein Modul beantragt"
                                                         " dem Modul Disma welcher jedoch nicht zugestellt wurde. An den richtigen Professor ging diese jedoch da dieser schon in Pension war trat der Antrag nicht inkraft. Diesen Ausgleich sieht der Student nicht als erforderlich solange es darum gehe sein Wissen welches um die Funktionsweise des"
                                                         "Themas gehe und nicht um Auswendiglern Wissen gehe."
                                                         , nodeBesondereUmstände)

        nodeStudiumUndArbeit = self.NodeGraphCreateSubTree("Studium und Arbeit",
                                                           "Normalerweise sollte das Arbeiten und dass Studium nicht in geflikt geraten da die Priorisierung dann meist auf der Einnahmequelle liegt und somit meist nur Maximal Zwei Kurse pro Semester bearbeitet werden. Wenn dies sich nun aber mit anderen Umständen"
                                                           " zusammen fügt kann es sein, dass entweder das Studium oder die Arbeit darunter leidet. Ein Kommulitone war 2020-2021 auch kurz davor gefeuert zu werden da er wegen dem extra Druck den Praktika mit Paralellen Abgabe zeiträumen ihm gegeben haben. Da er in jeder Gruppe"
                                                           " als Tragendes Mitglied mit arbeiten musste und somit die Zeit die er als Freizeit haben sollte zur Arbeit verwenden. Die Freie Zeit die er noch hatte abgesehen von Schlaf musste somit für Arbeit verwendet werden wwelche nur 1-2 Stunden pro WWoche."
                                                           , nodeBesondereUmstände)

        nodeStudiumMitBurnout = self.NodeGraphCreateSubTree("Studium mit Burnout",
                                                            "Ein heikles Thema ist Burnout immer, meines Verständnisses nach ist dies die Unfähigkeit zur Arbeit oder Ruhe aufgrund von stetigem Stress. Basierend auf dieser Definition meldete sich ein Student der seit 6 Semestern daran leidet .Diese Nacheffekte merkt"
                                                            " er momentan noch, was die späte bearbeitung seines Projektes und die späte bearbeitung seiner Reflektionen zu folge hat. Um stetige bearbeitung von solchen Projekten sicher zu stellen und trotzedm den Stresslevel niedrig zu halten wäre es hilfreich dies so wie bei dem Modul"
                                                            " MCI umzusetzen. Dies war überraschenderweise eine Gruppenarbeit, jedoch waren die Kontrollen immer mit Studentischer Hilfskraft um sicherzugehen dass die Gruppe gemeinsam arbeitet und um eine Reflektion der Arbeit zu geben. Zudem waren die Prüfer immer verständlich zu den"
                                                            " Privaten Problemen. Sie gingen zudem soweit, dass sie die Struktur der Abgaben bei begründung so um zu strukturieren. Diese Umstrukturierung ging rein um die Fristen und konnte gleich gut sicherstellen, dass die Prüfung bestanden werden kann. so schilderte er eine Lösung für"
                                                            " andere Module bei denen Personen Basierend auf Burnout scheitern."
                                                            , nodeBesondereUmstände)

        nodeStudiumWeiterEntfernt = self.NodeGraphCreateSubTree("Studium mit weiter Anfart",
                                                                "Studenten mit sehr langer Fahrzeit schilderten, dass sie von Online Vorlesungen stark Profitert haben. Ein Punkt der dies besonders zeigte war eine Schilderung eines Studenten der für die Abnahme eines Praktika die 15 Minuten maximal dauernte eine strecken von"
                                                                " 45 Minuten hin und 45 Minuten zurrück zurrück legen musste. Aufgrund seiner langen anfahrzeit und Benötigung eines Autos,da eine Zugfahrt nach Gummersbach für ihn 3 Stunden dauert, hat er sich mit der Struktur, dass nur das erste Semester Plicht in Präsents sei um Kontackte"
                                                                " zuknüpfen und sonst alle Vorlesungen über die THe-Learning Platform anbieten. Da er im Wintersemester 2019/2020 Täglich Präsent da sein musste um alles zu lernen musste er auch Privat immer viel Organisatorisch planen damit er für die Vorlesunge das Auto bekomme."
                                                                , nodeBesondereUmstände)

        nodeRevuluionDurchOnlineUni = self.NodeGraphCreateSubTree("Revulution durch Online Semester",
                                                                  ""
                                                                  , node)
    def NodeGraphCreateSubTree(self, name: string, description: string, parent: Node):
        node = Node(description, name)
        self.nodeList.append(node)
        node.connect(parent)

        return node

    def NodeGraphCreateFromTeamDeez(self, graph):
        ###################################################
        # Creating nodes
        ###################################################
        nodeMain = Node("Informationen rund ums Studium", "Main")
        #nodeMain.connect(paper_source_example_node)
        self.nodeList.append(nodeMain)

        #self.NodeGraphCreateProgrammingTree(nodeMain)
        #self.NodeGraphCreateAAAAAAATree(nodeMain)
        self.NodeGraphCreateOrganisationTree(nodeMain)
        ###################################################

        ###################################################
        # Registering nodes
        ###################################################
        for node in self.nodeList:
            graph.add_new_node_to_graph(node)
        ###################################################

    def create_demo_nodes(self, graph):
        """
        Diese Methode dient Ihnen also Demonstration für den Aufbau eines Graphen.
        TODO: Löschen oder kommentieren Sie diese Methode aus wenn Sie Ihren eigenen Graphen erstellen.
        """

        how_to_node = Node("Dies ist der Inhalt des Knotens. Ein Zeilenumbruch erfolgt automatisch. Wenn Sie "
                           "jedoch manuell einen Absatz einfügen möchten ist dies über \n \n möglich.\n \n"
                           " Sie haben die Möglichkeit Text als *kursiv* oder **fett** oder ***kombiniert*** "
                           "hervorzuheben.\n\n"
                           "Mit der ***Leertaste*** können Sie Ihren Graphen ausrichten lassen. Hierbei "
                           "wirken zwei Arten von  simulierten Kräften. Knoten stoßen sich generell ab "
                           "zum Zweck der visuellen Verteilung. Desto weiter Knoten voneinander entfernt "
                           "sind desto schwächer ist Abstoßungskraft. Knoten die miteinander verbunden sind "
                           "ziehen sich an. Desto weiter Knoten voneinander entfernt sind umso stärker ist "
                           "die Anziehungskraft.\n\n"
                           "Mit der ***T*** Taste können Sie die Titel der Knoten ein und ausblenden.\n\n"
                           "Mit der ***Esc*** Taste können Sie die Anwendung schließen.\n\n"
                           "Darüber hinaus können Sie Überschriften in drei Ebenen definieren. Text der als "
                           "Überschrift markiert wird, wird bis zum nächsten Zeilenumbruch als solcher "
                           "erkannt.\n"
                           "\n# Das ist Ebene 1\n"
                           "Nach einem Absatz wird eine Überschrift automatisch unterbrochen."
                           "\n## Das ist Ebene 2\n"
                           "Wie sie sehen ist diese Überschrift etwas kleiner."
                           "\n### Und abschließend Ebene 3\n"
                           "Und hier die kleinste Form.\n\n"
                           "\n# Hinweis\n"
                           "Wenn Ihr Graph wächst wird es immer schwieriger werden ihn zu "
                           "erweitern und zu verändern. Hier entsteht die Verbindung zu Softwareprojekten. "
                           "Zu beginn ist alles noch leicht nachvollziehbar und übersichtlich. Desto mehr "
                           "Funktionalität Sie jedoch implementieren um so komplexer wird Ihr System. "
                           "Es gibt immer mehr Inhalte und mehr Verbindungen dieser Inhalte. Erschaffen Sie "
                           "hierbei keine geeignete Struktur erhalten Sie was wir Spaghetti-Code oder einen "
                           "Big Ball of Mud nennen. Alles ist scheinbar miteinander verbunden und erzeugt "
                           "Abhängigkeiten miteinander. Wenn Sie ein Teil verändern wollen müssen Sie auch "
                           "alle anderen Teile verändern."
                           "Ein Teil Ihrer Aufgabenstellung ist es mit dieser wachsenden Komplexität "
                           "umzugehen. Sie entscheiden dabei als Team welchen Weg Sie einschlagen. Ziehen "
                           "sie es vor die Inhalte hard zu coden also direkt in diese Methode zu schreiben? "
                           "Werden Sie eigene Klassen und Methoden für die Bestandteile des Graphen anlegen? "
                           "Schreiben Sie selbst einen Importer über den Sie Text Files einlesen können?"
                           "Schreiben Sie ein User Interface um Texte direkt über die"
                           "Applikation einzugeben? Denken Sie dabei auch an Modelle und wie Abstraktion "
                           "Ihnen hilft Dinge zu vereinfachen. Planen Sie Ihren Graphen, teilen Sie "
                           "Verantwortlichkeiten im Team auf, erstellen Sie Modelle und iterieren Sie um"
                           "Ihren Wissensgraph inkrementell zu entwickeln."
                           ""
                           "\n# Bilder\n"
                           "Zu jedem Knoten können Sie ein Bild hinzufügen. Hier für ist es notwendig "
                           "das dieses Bild im Ordner Resources/Images abgelegt wird und der Name der Datei "
                           "als dritter Parameter spezifiziert wird. Denken Sie daran Bilder in Git "
                           "hinzuzufügen: Rechtsklick + Git + Add. Auch diese Bilder müssen Sie anschließend "
                           "commiten und pushen."
                           "\n # Verbindungen (Kanten) \n"
                           "Knoten können über die Methode .connect mit einander verbunden werden. Dabei "
                           "wird diese Methode auf dem Vater Knoten angewandt und das Kind als Parameter "
                           "übergeben, \n\nz. B.: ***vater.connect(kind)***\n\n"
                           "Wenn Sie im Graphen einen Knoten Verschieben, werden die Kinder immer "
                           "mit verschoben. Sie können auch bidirektionale Verbindungen anlegen in dem Sie "
                           "zusätzlich: *kind.connect(vater)* verwenden. Selektieren Sie einen Knoten, "
                           "werden alle Kinder und Kindeskinder im Graphen optisch hervorgehoben."
                           "\n # Menü \n"
                           "Das Menü oben links stellt Ihnen zwei Optionen zur Verfügung."
                           "\n ## Export \n"
                           "Der Export erlaubt es Ihnen den aktuellen Graph als ZIP File zu exportieren. "
                           "Dieser File ist Ihre Abgabe am Ende des Projektes. Neben dem Graphen werden auch "
                           "alle Bilder im Image Ordner exportiert."
                           "\n ## Import \n"
                           "Der Import erlaubt es einen exportierten Graphen zu laden. Wenn Sie EPI im POW Modus "
                           "besuchen können Sie auf diesem Wege die Graphen Ihrer Kommilitonen laden. Wenn Sie diese "
                           "Funktion verwenden möchten, achten Sie bitte darauf, dass Bilder im "
                           "importierten ZIP File in den Image Ordner Ihres Projektes importiert werden. "
                           "Falls ein File mit dem identischen Namen im Image Ordner bereits vorhanden ist, "
                           "wird der Name des importierten Bildes mit dem Namen Ihres Teams konkateniert/"
                           "verbunden.\n\n",
                           "Help Knoten: Dies ist der Titel Ihres Knotens",
                           "image_placeholder.png")

        online_source_example_node = Node("## Anmerkung: \n"
                                          "Dies ist Knoten für Online-Quellen. In diesem konkreten Fall für Markdown "
                                          "als Internet Quelle. Hierbei wird die offizielle Website des Entwicklers "
                                          "von Markdown verwendet. Eine Website als Quelle ist legitim, wenn sie "
                                          "bestimmte Kriterien der Glaubwürdigkeit und Zuverlässigkeit erfüllt. "
                                          "Kriterien hierfür sind: \n\n"
                                          "**- Expertise:**\n"
                                          "Überprüfen Sie, wer hinter der Website steht. Ist es eine anerkannte "
                                          "Institution, eine Bildungseinrichtung oder ein Experte auf dem Gebiet? \n\n"
                                          "**- Aktualität:**\n"
                                          "Überprüfen Sie das Datum der Veröffentlichung oder der letzten "
                                          "Aktualisierung. Für viele Themen ist es wichtig, dass die Informationen "
                                          "aktuell sind. \n\n"
                                          "**- Genauigkeit und Zuverlässigkeit:**\n"
                                          "Enthält die Website präzise Informationen, die mit anderen glaubwürdigen "
                                          "Quellen übereinstimmen? Websites, die sorgfältig recherchiert und mit "
                                          "Belegen untermauert sind, sind in der Regel vertrauenswürdiger.\n\n"
                                          "**- Zweck und Objektivität:**\n"
                                          "Beurteilen Sie den Zweck der Website. Ist sie darauf ausgerichtet, "
                                          "objektive Informationen zu liefern, oder verfolgt sie kommerzielle, "
                                          "politische oder ideologische Ziele? Objektive, unparteiische Quellen sind "
                                          "generell vertrauenswürdiger.\n\n"
                                          "**- Transparenz:**\n"
                                          "Gute Quellen bieten oft Informationen über ihre Autoren, Finanzierung, "
                                          "Mission und den Prozess der Inhaltsprüfung.\n\n"
                                          "\n## Beispiel\n"
                                          "\n### Autor:\n"
                                          "Gruber, John"
                                          "\n### Jahr:\n"
                                          "2004"
                                          "\n### Titel:\n"
                                          "Markdown"
                                          "\n### Verfügbar unter:\n"
                                          "https://daringfireball.net/projects/markdown/"
                                          "\n### Zugriff am:\n"
                                          "11. November 2023"
                                          , "(Gruber, 2004)")

        literature_source_example_node = Node("## Anmerkung: \n"
                                              "Dies ist Knoten für Literaturquellen. Hierbei sind folgende "
                                              "Informationen für ***Bücher*** essenziell:\n\n"
                                              "**- Autor:**\n Der vollständige Name des Autors.\n\n"
                                              "**- Erscheinungsjahr:**\n Das Jahr, in dem das Buch veröffentlicht "
                                              "wurde.\n\n"
                                              "**- Titel des Buches:**\n Der vollständige Titel des Buches, eventuell "
                                              "inklusive Untertitel.\n\n"
                                              "**- Auflage:**\n Inhalt kann sich mit den verschieden Auflagen "
                                              "eines Buches unterscheiden. Daher ist es wichtig die Auflage anzugeben, "
                                              "auf die Sie sich beziehen. \n\n"
                                              "**- Ort der Veröffentlichung:**\n Die Stadt, in der der Verlag seinen "
                                              "Sitz hat."
                                              "**- Verlag:**\n Der Name des Verlags.\n\n"
                                              "\n## Beispiel\n"
                                              "\n### Autor:\n"
                                              "Martin, R.C."
                                              "\n### Veröffentlichungsjahr:\n"
                                              "2021"
                                              "\n### Titel:\n"
                                              "Clean Craftsmanship: Disciplines, Standards, and Ethics"
                                              "\n### Auflage:\n"
                                              "1. Auflage"
                                              "\n### Ort:\n"
                                              "Boston"
                                              "\n### Verlag:\n"
                                              "Addison-Wesley Professional"
                                              , "(Martin, 2021)")

        paper_source_example_node = Node("Für wissenschaftliche Veröffentlichungen (***Paper***) sind folgende "
                                         "Angaben notwendig:\n\n"
                                         "**- Autor(en) des Papers:**\n Die Namen der Autoren, in der "
                                         "Reihenfolge, in der sie im Paper aufgeführt sind.\n\n"
                                         "**- Jahr der Veröffentlichung:**\n Das Jahr, in dem das Paper "
                                         "veröffentlicht wurde.\n\n"
                                         "**- Titel des Papers:**\n Der vollständige Titel des Papers.\n\n"
                                         "**- Titel der Zeitschrift oder Konferenz:**\n Der Name der Zeitschrift "
                                         "oder der Konferenz, in der das Paper veröffentlicht wurde.\n\n"
                                         "**- Bandnummer(Ausgabennummer):**\n Die Band- und Ausgabennummer der "
                                         "Zeitschrift, in der das Paper erschien.\n\n"
                                         "**- Seitenzahlen:**\n Die Seitenzahlen des Papers in der Zeitschrift."
                                         "**- URL:**\n Falls das Paper online verfügbar ist, fügen Sie die URL "
                                         "hinzu.\n\n"
                                         "**- Zugriff am:**\n Das Datum, an dem Sie auf das Paper zugegriffen "
                                         "haben, falls es online verfügbar ist.\n\n"
                                         "\n## Beispiel\n"
                                         "\n### Autor:\n"
                                         "Dijkstra, E.W."
                                         "\n### Veröffentlichungsjahr:\n"
                                         "1972"
                                         "\n### Titel:\n"
                                         "The Humble Programmer"
                                         "\n### In:\n"
                                         "Communications of the ACM"
                                         "\n### Bandnummer(Ausgabennummer):\n"
                                         "15(10)"
                                         "\n### Seitenzahlen:\n"
                                         "859-866"
                                         , "(Dijkstra, 1972)")


        how_to_node.connect(online_source_example_node)
        how_to_node.connect(literature_source_example_node)
        how_to_node.connect(paper_source_example_node)

        graph.add_new_node_to_graph(how_to_node)
        graph.add_new_node_to_graph(online_source_example_node)
        graph.add_new_node_to_graph(literature_source_example_node)
        graph.add_new_node_to_graph(paper_source_example_node)
