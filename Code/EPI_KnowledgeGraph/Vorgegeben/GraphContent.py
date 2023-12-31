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
    # 30.000 symbols per Member
    # ~~=> 1500 symbols per node

    # Demands to group
    # 3 x 20 nodes       = 60 nodes
    # 3 x 30.000 symbols = 90.000 symbols

    def __init__(self, graph: Graph):
        self.NodeGraphCreateFromTeamDeez(graph)
        #self.create_demo_nodes(graph)

    def NodeGraphCreateProgrammingTree(self, parrant : Node):

        nodeProgramming = self.NodeGraphCreateSubTree(
            "Programming",
            "Dateien werden in unterschiedlich Formaten gespeichert, je nach dem wie man diese nutzen möchte."
            "Hier sind entweder **Text** vasiert oder auch **Binär**. Beide mit ihren vor und nachteilen.\n"
            "Zusätzlich gibt es auch gemischte formate, "
            "da das lesen und schreiben dieser Formate aber ehr unkomfortabel ist, wird die nutzung ehr vermieden",
            parrant)

        nodeDataFormat = self.NodeGraphCreateSubTree(
            "Dateiformat",
            "Dateien werden in unterschiedlich Formaten gespeichert, je nach dem wie man diese nutzen möchte."
            "Hier sind entweder **Text** vasiert oder auch **Binär**. Beide mit ihren vor und nachteilen.\n"
            "Zusätzlich gibt es auch gemischte formate, "
            "da das lesen und schreiben dieser Formate aber ehr unkomfortabel ist, wird die nutzung ehr vermieden",
            nodeProgramming)
        nodeBinary = self.NodeGraphCreateSubTree(
            "Binary",
            "## Info\n"
            "In diesem Format werden Daten sehr Kompakt direkt an einander gereiht gespeichert. Hier "
            "wird auf Menschlich nützliche elemente verzichttet und der Nutzen der Machiene erhöht."
            "Hier kann es oftmals dazu kommen das die Daten so kompakt sind, das es sehr aufwenig ist diese "
            "Daten zu dekomplemieren. Es gibt zahlreiche Algorithmen und formate die dies ermöglichen."
            "Manche Formate bieten zudem eine Qualitätsstufte, damit kann nicht nur die Qualität gesteuret "
            "werden sondern auch die Komplexität und den damit zusammenhängenden Aufwand.\n\n"
            "Als Weiterens haben Binär Dateien das Problem, das wenn die Datei auch nur leicht "
            "Fehlerhaft ist, es mit erhöhter Warscheinlichkeit dazu führen kann das die Datei nicht mehr lesbar ist."
            "Wenn dies geschied ist es fast unmöglich diese Datei wieder her zu stellen."
             "## Vorteile\n"
            "- Einfacher zu lesen und zu schreiben als Text basierte Dateien\n"
            "- Das Format ist effizienter in der Speicherung\n"
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
            "Eines der bekanntesten Musik Formate\n"
            "### Abhänigkeiten\n"
            "- ID3\n"
            "### Vorteile\n"        
            "- Sehr verbreitet\n"
            "### Nachteile\n"
            "- Bis 2013 nur mit lizens nutzbar\n"
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
            "Ein weniger genutzes aber einfach zu lesendes 3D-Model format oft genutzt "
            "in kleineren Projekten aber auch in der lernphase von game engine development\n"
            "### Abhänigkeiten\n"
            "- MTL\n"
            "### Vorteile\n"      
            "- Einfach zu lesen/Schreiben"
            "### Nachteile\n"
            "- Ungenau/verwirrend definierte format regeln"
            "## Links\n"
            "Wikipedia : https://en.wikipedia.org/wiki/Wavefront_.obj_file",
            nodeBinary)
        self.NodeGraphCreateSubTree(
            "OGG",
            "# Ogging Musik Datei\n"
            "## Info\n"
            "Ein offener Standard for Musik und Sound Dateien."
            "Oft verbreitet aber geschichtlich von MP3 dominiert und in der moderne von andren Formaten.\n"
            "### Abhänigkeiten\n"
            "### Vorteile\n"     
            "- Offener Standard"
            "### Nachteile\n"
            "- Kompliziertes Format"
            "## Links\n"
            "Wikipedia : https://en.wikipedia.org/wiki/Ogg",
            nodeBinary)
        self.NodeGraphCreateSubTree(
            "PDF",
            "# Portable Document Format\n"
            "# [ISO 32000]\n"
            "## Info\n"
            "Die PDF Dateien haben schon lange den Standard in Dokumenten erreicht. "
            "Kaum findet man Dateien die nicht in diesem Format bereitgestellt werden. "
            "Egal ob Bestellungen, Rechnungen oder Dokumentationen, alle werden als PDF über das netzt verteilt."
            "### Abhänigkeiten\n"
            "- XML Parser\n"
            "### Vorteile\n"
            "- Sehr verbreitetes und unterstützes Format\n"
            "### Nachteile\n"
            "- Sehr komisch zu lesen da das Format halb Binär und halb Text ist.\n"
            "## Links\n",
            nodeBinary)
        nodePNG = self.NodeGraphCreateSubTree(
            "PNG",
            "# Portable Network Graphics\n"
            "# [RFC 2083]\n"
            "## Info\n"
            "PNG Dateien sind einer der bekanntesten Bild Formate. Da PNG neben JPEG der bessere Standard ist."
            "Daten die man als PNG verschickt behalten ihre Qualität für immer auf, sofern "
            "Sie nict zwischendrin zu einer JPEG Datei umkonvertiert worden ist.\n\n"
            "Zu PNG gehört auch ein großes Merkmal, die Transparenz. Da Bitmaps oftmals "
            "nicht mit transparenz unterschtützt werden ist dieses Format immer der Weg.\n\n"
            "Leider aber ist das PNG Format sehr komplex zu laden, das aber nicht zum vollen."
            "Der inhalt einer PNG Datei besteht im genauen aus blöcken mit ihren ID nummern "
            "und der Pixeldaten die mit dem ZLIB format verpackt sind. Um die Pixeldaten "
            "also lesen oder schreiben zu können benötigt man diesen Algorithmus zuerst."
            "### Abhänigkeiten\n"
            "- ZLIB"
            "### Vorteile\n"
            "- rellativ kleine größe\n"
            "- verlustfrei\n"
            "### Nachteile\n"
            "- Extrem komplexe laden und speichern\n"
            "## Links\n"
            "Wikipedia : https://en.wikipedia.org/wiki/PNG",
            nodeBinary)
        self.NodeGraphCreateSubTree(
            "JPG",
            "# Joint Photographic Experts Group\n"
            "# [ISO/IEC 10918]\n"
            "## Info\n"
            "JPEG ist eines der meist genutzen Formate im Internet\n"
            "Einerseits ist die Qualität wirklich nicht die beste und durch mehrfaches verschicken "
            "wird sie auch immer schlechter, dennoch ist es genau wegen der winzigen größe so "
            "das dieses Format so weigehend genutzt wird.\n\n"
            "Das was JPEG aus macht ist die verlustreiche Kompression. Das bedeutet zwar das "
            "sehr viel Information verloren geht, womit das Format verständlicherweise "
            "bei grafikern unbeliebt ist, jedoch ist es für den normalgebrauch Wunderbar da es im "
            "vergleich kaum Speicher einnimmt.\n"
            "### Abhänigkeiten\n"
            "- Huffman\n"
            "### Vorteile\n"
            "- Sehr geringe speicherauslastung\n"
            "### Nachteile\n"
            "- Etwas aufwendiges Laden/Speichern"
            "- Qualität rellativ schlecht"
            "## Links\n"
            "Wikipedia : https://en.wikipedia.org/wiki/JPEG",
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
            "# Programmier Sprachen"
            "## Info\n"
            "In der Programmierung gibt es zahlreiche Spracharten, noch viel mehr "
            "verschiedene Sprachen und noch viel mehr Dialekte. Die auswahlt "
            "ist enorm. "
            "### Abhänigkeiten\n"
            "- Interpretierungs Machine\n"
            "### Vorteile\n"
            "- Sprachen helfen und unterstützen dem Menschen mit anderen Menschen "
            "zu kommunizieren aber auch mit Maschinen\n"
            "### Nachteile\n"
            "- Probleme in einer Sprache können missverständnisse aufbringen."
            "- Fehlende Sprachkunst kann sich stark negativ auf die Qualität auswirken\n"
            "## Links\n",
            nodeProgramming)
        nodeMachineLanguage = self.NodeGraphCreateSubTree(
            "Machine Language",
            "# Die Sprache der Machine\n"
            "## Info\n"
            "Oft wird Assembly und MAschinensprache verwechselt, aber da gibt "
            "es einen kleinen unterschied. Maschienensprache bezieht sich auf die "
            "exakten bytes die in einem Programm oder auch eineer Bibilotek befinden."
            "Assembly auf der anderen Seite ist nur eine kleine Abstaktion auf "
            "mehr verständlichere und menschlich lesbare elemente.\n\n"
            "Assembly bleibt und ist einer der einzigen wege das komplette maximum "
            "aus einer hardware heraus zu bekommen. Der Grund aber, warum dies trotz den "
            "Positiven eigenschaften ehr kaum direkt genutzt wird ist, dass das "
            "Eigentliche Programmieren in Assembly sehr mühsam ist. Da einzelne Befehle "
            "nur sehr minimale Effekte haben, braucht man eine menge Code um alleine "
            "kleine Sachen zu verarbeiten.\n\n"
            "Aus diesem Grund wurden zahlreiche Sprachen entwickelt die Assembly "
            "abstraktieren und damit eine noch einfachere Umgebung schaffen. "
            "Hier ist aber darauf zu achten das man sich mit jeder abstaktion "
            "weiter von dem tatsächlichen Hardwarecode entfernt."
            "Letzendlich wird jeder Code am Ende in Machinencode ausgeführt."
            "Im besten Fall ist die Lösung in einer Höheren Sprache besser oder das gleiche "
            "wie als hätte man diesen selbst in Assembly geschrieben.",
            nodeLanguage)
        self.NodeGraphCreateSubTree(
            "x86",
             "## Info\n"
            "Ist eine Assembly Sprache die 1978 mit dem Intel 8086 eingefürt worden ist.\n"
            "Eine große stärke dieser Sprache ist der Fokus auf complexe Befehle."
            "Die macht die Sprache natürlich deutlich Komplexer kann aber durchaus dies deutlich "
            "in performance wieder gut machen. In den vergangenen Jahrzehnten "
             "hat sich diese Sprache als Felsenfester standard durchgesetzt."
             "Auch wenn einige sich immer wieder aufregen das die Sprache viel zu aufgebläht ist und "
             "damit viel zu aufwenig und kompliziert wird, ist bis heute keine alternative auf dem Markt."
             "Zwar ist ARM durchaus in Geräten heufiger genutzt, ernüchtert diese Zahl aber wenn man"
             "genauer hinsieht und erblickt das ARM fast allen fällen nur im Mobilen Mark steckt "
             "wo x86 auf allen Destop computern zu finden ist"
            "### Vorteile\n"
            "- Selbst Komplexe Befehle, falls unterstützt, können genutzt werden\n."
            "### Nachteile\n"
            "- Sehr Komplexe Sprache\n"
            "- Hardware ist sehr aufwenig herzustellen\n"
            "## Links\n"
            "Wikipedia : https://en.wikipedia.org/wiki/X86\n",
            nodeMachineLanguage)
        self.NodeGraphCreateSubTree(
            "ARM",
            "## Info\n"
            "ARM wurde erschaffen um ein Konkurent gegen die großeren Namen in der Scene zu sein "
            "aber nicht um direkt auf einem Level mit ihnen zu Kämpfen, sondern effizeinter und "
            "günstiger zu sein. Dadurch ist ARM mehr lucktativ für den normal verbraucher und in "
            "der Industrie für den normalen arbeitsplatz.\n\n"
            "ARM ist am verbreitesten in portablen Geräten, aber auch kleineren Mediengeräten "
            "im Haushalt."
            "### Vorteile\n"
            "- Geringer Stromverbrauch\n"
            "- Günstige herstellung der Hardware\n"
            "### Nachteile\n"
            "- Inkompartibel mit x86"
             "## Links\n"
            "Wikipedia : https://en.wikipedia.org/wiki/ARM_architecture_family",
            nodeMachineLanguage)
        self.NodeGraphCreateSubTree(
            "MIPS",
            "# Microprocessor without Interlocked Pipelined Stages\n"
            "## Info\n"
            "Ähnlich wie ARM, wurde dies als Ziel der Reduced Instruction set "
            "computer (RISC) Architektur erschaffen. Da ARM aber mit seiner "
            "Effizienz besser da steht und x86 deutlich stärker ist, ist MIPS "
            "nur noch in sehr kleinen und bestimmten Embedded umgebungen zu finden.\n"
            "Früher wurden einige Geräte ehr mit MIPS ausgestattet als mit ARM, "
            "da zu dem Zeitpunk ARM nicht so gut war. Seit 2011 hat sich dies "
            "aber stark geändert und überschattet nun den Markt mit einem besseren Produkt"
            "### Vorteile\n"
            "- Mehr leistung unter gewissen Bedinungen\n"
            "### Nachteile\n"
            "- Deutlich weniger unterstützung durch Software\n"
            "## Links\n"
            "Wikipedia : https://en.wikipedia.org/wiki/MIPS_architecture",
            nodeMachineLanguage)

        nodeDataOriented = self.NodeGraphCreateSubTree(
            "Data Oriented",
            "# Daten Orentierte Sprachen"
            "Diese Art von Sprachen wird oft unterschätzt aber ist ein Grundpfeiler für "
            "Datenverarbeitung aller Art. In modernerer Zeit wird heufiger über die "
            "Estetik von Code geredet und kaum noch was für auswirkungen dieser Code "
            "auf die Hardware hat. Durch diese Entscheidung passiert es sehr heufig "
            "das Programme oft von Grund auf schlecht entwickelt werden und später "
            "dies nicht mehr rückgänig gemacht werden kann."
            "In diesen Fällen fällt das Problem an, das man ein System hat was "
            "Probleme bereitet, das man aber nicht verbessern kann.\n\n"
            "Der riesen Vorteil in Daten Orentierte Sprachen liegt also darin, dass man "
            "sich mehr um die Daten kümmernt und dem Programmierer mehr bewusst ist was "
            "die Konsequenzen des Codees sind.\n\n"
            "In vergangener Zeit hatten Computer kaum hardware Resourcen und man musste "
            "mit viel mühe es überhaupt schaffen sein Teil von dem was man erstellen "
            "möchte zum laufen zu bringen. Heute ist es aber so, das wir so viele "
            "Resoucen besitzen, nicht nur Hardware aber auch Software und Netzwerk."
            "Es ist also heutzutage sehr viel einfacher Code zu schreiben, da man sich "
            "sicher gehen kann das jeder genügend Arbeitspeicher besitzt,  "
            "einen Prozessor besitzt der schnell genug ist, eine Festplatte die "
            "genügend Speicher hat oder sei es, das es Irgend eine Hardware gibt "
            "die nicht gut genug währe.",
            nodeLanguage)
        self.NodeGraphCreateSubTree(
            "C",
            "## Info\n"
            "Zuerst erschienen in 1972 aber erst wirklich durchgesetzt in 1989/1990 ist "
            "C einer der Grundpfeiler der heutingen Computertechnik. Trotz allem wird diese Sprache von dem meisten "
            "ermüdigent angesehen, da sie nicht gerade freundlich für Anfäger ist. Aus diesem aber "
            "auch mehreren Gründen werden viele andere Sprachen bevorzugt.\n"
            "### Abhänigkeiten\n"
            "- Kompartibler Kompiler\n"
            "### Vorteile\n"
            "- Sehr minimalistische Sprache\n"
            "- Einfach zu lernen\n"
            "- Hohe kontrolle über Daten\n"
            "### Nachteile\n"
            "- Man kann schnell in komplizierte fehler kommen die nicht leicht verständlich für anfanger sind.\n"
            "- Mühseliger als andere Sprachen\n"
            "- nahezu kaum Standard Bibiloteken (nur POSIX)\n"
            "## Links\n"
            "Wikipedia : https://en.wikipedia.org/wiki/C_(programming_language)\n",
            nodeDataOriented)
        nodeCPP = self.NodeGraphCreateSubTree(
            "C++",
            "## Info\n"
            "C++, wie der name schon verät ist eine Erweiterung von C.\n"
            "Bjarne Stroustrup entwickelte C++ um Funktionen aus anderen nicht so "
            "gelungenen Sprachen heraus zu nehmen, zu verbessen und sie dann in C ein zu bauen. "
            "Somit entstand langsam die Sprache **C mit Klassen**. Mit mehr Erweiterungen und "
            "Verbesserungen wurde es dann zu C++."
            "### Abhänigkeiten\n"
            "- Kompartibler Kompiler\n"
            "### Vorteile\n"
            "- Verbesserter Syntax\n"
            "- Generische Typen können genutzt werden\n"
            "- Strukturen, jetzt Klassen, können Funktionen enthalten\n"
            "- Funktionen können Überlanden werden\n"
            "### Nachteile\n"
            "- Vererbungen können, wie auch in anderen Sprachen, komplexe interaktive Fehler enstehen lassen\n"
            "## Links\n"
            "Wikipedia : https://en.wikipedia.org/wiki/C%2B%2B\n",
            nodeDataOriented)

        nodeObjectOriented = self.NodeGraphCreateSubTree(
            "Object Oriented",
            "# Objekt Orientiertes Programmieren\n"
            "## Info\n"
            "Auch wenn man in jeder Sprache Objekte generell nutzt, werden damit ehr Sprachen "
            "bezeichnet die viel genauer mit Objekten umgehen. In Sprachen wie C und C++ werden "
            "alle informationen von Objekten fallen gelassen. Damit sind die Programme deutlich "
            "kleiner. Als Nachtwil natürlich gibt es keine Informationen über enthaltene Objekte "
            "und deren Struktur. Hier enstehnt nun das mögliche Problem das man währen der Laufzeit "
            "an genau diese Informationen möchte, in nich Objekt orientieten Sprachen geht soetwas nicht.\n"
            "Mit genau dem selben Punkt ist es also auch möglich, wenn man diese Informationen gespeichert "
            "hat, während der Laufzeit Objekte zu erstellen oder auch zu analysieren."
            "### Vorteile\n"
            "- Verbesserte Strukturierung von Logischen zusammenhängen\n"
            "- Objekte haben eine Identität"
            "- Umgang mit der existenz von Objekten und deren Indentität\n"            
            "### Nachteile\n"
            "- Hohe Gefahr Objekte zu komplex zu Erstellen\n"
            "- Code explodiert in Komplexität",
            nodeLanguage)
        self.NodeGraphCreateSubTree(
            "Java",
            "## Info\n"
            "Java ist eine Sprache die Entwickelt worden ist um eine sichere Sprache zu "
            "erschaffen die es Programmen erlaubt auch bei einem größeren Fehler nicht ab zu stürtzen. "
            "Zudem war ein großer Punk das diese Programme auf all möglicher Hardware laufen soll."
            "Die Idee hinter Java war, das man nur die Virtuelle Machine erstellen muss, und jedes "
            "Java Programm kann auf ihr laufen. Damit sind die meisten Probleme behoben die zu der Zeit "
            "mit den Betriebsystem kriegen und ihrere inkompartibilität zwischeneinander gelößt scheint."
            "Im laufe der Zeit konnte sich Java mit großer stärke als beliebteste Sprache durchsetzen, "
            "Auch wenn die Vorteile von Java den normal nutzer nicht awirklich viel bietet. So umso mehr "
            "hat der effekt in der Industrie eine Ära definiert. Selbst heute noch beforzugen Firman Java "
            "vor anderen Sprachen. In den letzeren Jahren hat Java dennoch viel Negative Kritik bekommen da "
            "die Sprachwelt sich weg von Interativen und Objektorientierten Sprachen bewegt und Skriptsprachen "
            "immer mehr und mehr beforzugt werden. Dies gillt aber nur für kleinere Projekte. "
            "Für große Projekte wird immernoch Java beforzugt, auch wenn es seit längerem eine alternative "
            "gibt namens Kotlin. Diese Funktioniert läuft genauso auf der Virtuellen Machine wie Java auch. "
            "Somit muss also nicht auf eine neue Machine umgestiegen werden und der Umsprung kann direkt "
            "passieren. Android hat in den meisten fällen die auch schon getan."
            "Java wurde früher oft in kleineren Gertäten genutzt. "
            "Dazu gehören Fernsehr, Fernbedinungen, Boxen für das Karbelversehn aber auch viele viele mehr. "
            "Da bei falscher programmierung oder sogar einem größeren Fehler das ganze system absturtzen kann, wurde "
            "Java anstelle von C genutzt, um mit Hilfe der Virtuellen Machine diese Fatalen Fehler mit dem "
            "mit entwickelten StackTrace und weiteren Detailierten infomationen abfagne zu können. "
            "Mit diesen Infomationen über die Fehlzustände die Übersendet werden können, können Fehler deutlich besser "
            "nachvollzigen werden und damit auch ausgebessert werden."
            "Mit dieser Automatisierten Fehlersammelung und der Modifikation von einem Laufenden System konnte "
            "Software Qualität deutlich besser überwacht und ausgebessert werden\n"
            "### Abhänigkeiten\n"
            "- Java Virtuelle Maschine (JVM)\n"      
            "- Kompartibler Kompiler\n"       
            "### Vorteile\n"
            "- Durch die Nutzung einer Abstaktion durch die Java Virtuelle Maschine (JVM) ist "
            "es möglich das Code auf jedem System nahezu gleich läuft"
            "### Nachteile\n"
            "- Da der Code nicht nativ laufen kann, muss immer eine Java Virtuelle Maschine (JVM) genutzt werden\n"
            "- Der Garbage Collector ist bekannt dafür nicht effizient zu sein und bei einem großen Projekt "
            "wird dieser ein Problem\n"
            "## Links\n"
            "Wikipedia : https://en.wikipedia.org/wiki/Java_(programming_language)",
            nodeObjectOriented)
        self.NodeGraphCreateSubTree(
            "C#",
            "## Info\n"
            "C# ist eine weiterführung der Sprache C++. Daher könnte man auch erkennen, das das # "
            "für ein 2x2 Plus steht. Also anders gesagt ist das C++++.\n"
            "Die Idee hinter C# war im grunde nur \"Java aber von Microsoft\". Somit also "
            "hat sich Mirosoft daran gesetzt eine Java ähnliche Sprache zu entwickeln."
            "Dennoch, anders als Java, wurde C++ ehr als inspiration gezogen als andere Sprachen."
            "Somit ist C#, wie der name auch schon verät, mehr an den C Sprachen angelehnt."
            "Wie auch in Java, wird eine Virtuelle Machine genutzt. Hier nennt sich diese dot-NET"
            "Anders als in Java ist es möglich geteiile Bibiloteken (DLLs) zu nutzen."
            "Damit ist es möglich einen Brücke zu code aus anderen Sprachen zu schaffen."
            "Somit ist es also auch möglich allen perfomanten code in Beispielsweise C zu schreiben "
            "Und diesen dann in C# auf zu rufen."
            "### Abhänigkeiten\n"
            "- .NET Klassisch, Framework oder Core runtime"
            "### Vorteile\n"
            "- Sehr angenehme integration mit dem System\n"
            "- Möglichekeit code aus in C compilierten Bibiloteken auf zu rufen\n"
            "### Nachteile\n"
            "- Interaktionen die nicht bedacht wurden, sind sehr schlecht und notdürftig implementiert\n"
            "- Chaotische vielfallt von runtimes"
            "## Links\n",
            nodeObjectOriented)
        self.NodeGraphCreateSubTree(
            "VB.Net",
            "",
            nodeObjectOriented)

        nodeCPP.connect(nodeObjectOriented)

        nodeFunctional = self.NodeGraphCreateSubTree(
            "Functional",
            "# Funktionale Sprachen\n"
            "Funktionale Sprachen nutzen eine spizielle eigenschaft indem nur Funktionen genutzt "
            "werden die eine Gewisse Menge annimmt und einen Teil davon wieder zurück gibt\n"
            "In interativen Spachen ist oftmals der vergleich zu puren Funktionen."
            " Hier ist der Vorteil das diese Funktionen keinen Zustand besitzen und somit keine "
            "Veränderungen an Objekten darstellen, da diese deutlich schwerer zu testen sind und somit "
            "bei tests ehr unerwünscht sind.",
            nodeLanguage)
        self.NodeGraphCreateSubTree(
            "Haskell",
            "",
            nodeFunctional)

        nodeScript = self.NodeGraphCreateSubTree(
            "Script",
            "# Skript Sprachen\n"
            "Anders als Code der Kompiliert werden muss, können Skripte direkt mit einem Interpretations "
            "program ausgeführt werden. Dadurch kann der Code mehr portierbar sein und damit zu unterstützung diehnen "
            "Code auf verschiedenen Geräten gleich laufen zu lassen.",
            nodeLanguage)
        self.NodeGraphCreateSubTree(
            "Bash",
            "# Linux Bash Script\n"
            "Die bekannte Linux Bash ist die Konsole für alle Linuxs Varrianten. "
            "Hierzu dient das Script was die ausführung dieser Automatisiert",
            nodeScript)
        self.NodeGraphCreateSubTree(
            "PowerShell",
            "Eine neuere version der Windows Eingabeaufforderung.\n"
            "Sie enthällt mehr Funktionen als sein vorgänger und ermöglicht auch Skripte direkt zu nutzen.",
            nodeScript)
        self.NodeGraphCreateSubTree(
            "CMD",
            "# Windows Eingabeaufforderung\n"
            "Die Windows Commandline ist, wie man sie auch schon seit DOS kennt, die bekannte Schwarze Konsole.",
            nodeScript)
        self.NodeGraphCreateSubTree(
            "VBS",
            "# Visual Basic Script\n"
            "Dies ist eine Script Form von VisualBasic.NET. Dies wird meist in Excel als Makro funktionen genutzt\n"
            "### Vorteile\n"
            "- Einfach zu schreiben\n"
            "### Nachteile\n"
            "- Sehr gerinnge sicherheit"
            "- Wird sehr heufig für hacker angriffe genutzt",
            nodeScript)

        nodeRelational = self.NodeGraphCreateSubTree(
            "Relational",
            "# Relationale Sprachen\n"
            "Relationale Sprachen arbeiten, anders als bekannte iterative Sprachen, mit Mengen an Daten.\n",
            nodeLanguage)
        self.NodeGraphCreateSubTree(
            "SQL",
            "# Structured query language\n"
            "SQL ist die standardsprache wenn es um Datenbanken geht.\n"
            "Mit dieser Sprache geht es anders vor als mit anderen Sprachen, es wird komplett anders "
            "Gedacht und man geht immer nur auf die Mengen ein die man sich auf der Datenbank ließt und schreibt.\n\n"
            "Da man aber mit einer Menge von Daten hantiert trägt man auch eine große verantwortung."
            "Es kann sein, das man mit einer falschen aktion einen ganzen Seerver lahm legen kann. "
            "Egal ob man uasversehen alle Daten löscht oder sich eine riesige Datenbank selbst ausgibt und man Studnen warten muss"
             "### Vorteile\n"
            "- Es können unbegenzt viele Fragen an die Daten gestellt werden\n"
            "### Nachteile\n"
            "- Schwere übersichtlichkeit\n"
            "- Limitiert auf Daten\n",
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
            nodeProgramming)
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
            "Jedoch ist es möglich, das durch das aufblähen des Heaps und des Stacks zugleich eine kollision entsteht"
            "### Vorteile\n"
            "- Dynamische erzeugung von Speicher\n"
            "### Nachteile\n"
            "- Aufwenige Regestrierung der Speicherbereiche\n"
            "- Mägliche ineffiziente Nutzung durch schlechtes Design",
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

        nodeAlgoritm = self.NodeGraphCreateSubTree("Algorithms", "", nodeProgramming)
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
            nodeProgramming)
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
            nodeProgramming)
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
                                                "Manche Kurse sind Pflicht, während andere Wählbar sind jedoch sind nicht alle kurse anderer Studiengänge wählbar."
                                                "Eine bessere Konfigurierung des Studiums wie im Master ist Stark wünschenswert (auch von andern Kommilitonen)"
                                                "Zudem ist die Errechnung der Bearbeitungsdauer/ETC-Punkte teilweise sehr Unstimmig da zum Beispiel eine Bachelorarbeit 12 Punkte gibt und alleine"
                                                "die Einarbeitung in diese schon solange dauern kann."
                                                , node)

        nodeBachelorarbeit = self.NodeGraphCreateSubTree("Bachelorarbeit",
                                                         "Eine Bachelorarbeit wird meist als Ende des Bachelorstudiums gesehen jedoch stimmt dies nicht wirklich.Diese kann normalerweise"
                                                         " ab Sammlung der hälfte der zum Abschluss benötgen ETC-Punkte beantragt werden (Referenziert von einem Studenten der Uni Siegen)."
                                                         "Die Bewertung der Bachelorarbeit mit 12 ETC-Punkten ist von einigen Studenten fraglich unter der bedingung dass ein ETC-Punkt 30 Stunden Arbeit entsprechen."
                                                         "Aus berrichten anderer Studenten auch an anderen Universitäten sind diese 360 Stunden als minimum zum Schreiben und Formulieren der Bachelorarbeit zu verplanen."
                                                         "Durch diesen Unterschied wird von Studenten oftmals die Bearbeitund der Bachelorarbeit erst Beantragt wenn diese schon Fertig durchgeführt und geschrieben ist um nicht"
                                                         " den 9 oder 12 Wochen bearbeitungszeitraum zu überschreiten."
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

        self.NodeGraphCreateProgrammingTree(nodeMain)
        self.NodeGraphCreateAAAAAAATree(nodeMain)
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
