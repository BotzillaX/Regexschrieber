import time
import re

def evaluate_regex_performance(pattern, text):

    regex = re.compile(pattern)
    
    start_time = time.perf_counter()
    match = regex.search(text)
    end_time = time.perf_counter()
    
    elapsed_time = end_time - start_time
    
    return elapsed_time, match

def main():
    pattern = r"([\s\S]*?)hallo"
    text = """Es war einmal ein kleines Dorf in einem malerischen Tal, umgeben von hohen Bergen und dichten Wäldern. Dieses Dorf, das auf den ersten Blick unscheinbar wirkte, hatte eine lange und faszinierende Geschichte. Die Menschen, die dort lebten, waren seit Generationen eng mit der Natur und den alten Traditionen verbunden. Jeder Baum, jeder Fluss und jeder Berg hatte seine eigene Legende, die von den Dorfbewohnern eifrig weitergegeben wurde.

In diesem Dorf lebte ein alter Mann namens Hans, der für seine Geschichten bekannt war. Hans hatte ein langes und bewegtes Leben geführt und war in seiner Jugend weit gereist. Nun verbrachte er seine Tage damit, den Kindern des Dorfes von seinen Abenteuern zu erzählen. Seine Geschichten waren voller Magie, fremder Länder und außergewöhnlicher Begegnungen. Die Kinder versammelten sich oft um das knisternde Lagerfeuer, lauschten gespannt und stellten sich die bunten Bilder vor, die Hans mit seinen Worten malte.

Eines Abends, als die Sonne hinter den Bergen verschwand und die ersten Sterne am Himmel auftauchten, erzählte Hans eine besonders fesselnde Geschichte. Es war die Geschichte eines mutigen jungen Mannes namens Johann, der aufbrach, um das Geheimnis eines verborgenen Schatzes zu lüften. Johann war kein gewöhnlicher junger Mann; er war klug, stark und hatte ein unerschütterliches Herz. Seit seiner Kindheit hatte er von dem Schatz gehört, der tief in den Bergen versteckt sein sollte, bewacht von mächtigen Kreaturen und geschützt durch uralte Zauber.

Johann begann seine Reise mit nichts als einem alten Kompass und dem Segen seiner Eltern. Die Wege waren steinig und gefährlich, doch Johann schritt entschlossen voran. Er durchquerte dichte Wälder, kletterte über steile Felsen und überquerte reißende Flüsse. Auf seinem Weg begegnete er vielen wundersamen Wesen – sprechenden Tieren, freundlichen Riesen und weisen alten Eremiten, die ihm Rat und Hilfe gaben.

Eines Tages, nachdem er viele Prüfungen bestanden hatte, stand Johann schließlich vor der letzten Herausforderung: einer riesigen Höhle, die von einem gewaltigen Drachen bewacht wurde. Der Drache war alt und weise, aber auch sehr misstrauisch gegenüber Fremden. Johann wusste, dass er den Drachen nicht mit Gewalt besiegen konnte. Stattdessen setzte er sich hin und erzählte dem Drachen von seiner Reise, von den Wundern, die er gesehen hatte, und den Menschen, die ihm geholfen hatten. Der Drache, beeindruckt von Johanns Mut und Ehrlichkeit, entschied sich, ihm zu vertrauen und ließ ihn passieren.

In der tiefsten Kammer der Höhle fand Johann den Schatz – eine Truhe, gefüllt mit Gold, Juwelen und alten Schriftrollen, die das Wissen vergangener Generationen enthielten. Doch der wahre Schatz war nicht das Gold oder die Juwelen, sondern das Wissen und die Weisheit, die Johann auf seiner Reise gesammelt hatte. Mit einem vollen Herzen und einem neuen Verständnis für die Welt kehrte Johann in sein Dorf zurück.

Hans beendete seine Geschichte, und die Kinder saßen still da, fasziniert von den Abenteuern des jungen Johann. Die Flammen des Lagerfeuers warfen tanzende Schatten auf ihre Gesichter, und für einen Moment schien es, als ob die Magie der Geschichte lebendig geworden wäre. Hans lächelte und schaute in die Sterne. Er wusste, dass die Geschichten, die er erzählte, nicht nur Unterhaltung waren, sondern auch wichtige Lektionen und Weisheiten enthielten, die die Kinder ihr Leben lang begleiten würden.

Das Dorf, eingebettet in die Ruhe der Nacht, schien in diesem Moment ein wenig heller zu leuchten, erfüllt von den Träumen und Hoffnungen derer, die es bewohnten. Und so ging das Leben weiter, von Generation zu Generation, mit neuen Geschichten, neuen Abenteuern und einer nie endenden Verbindung zur Magie der Welt um sie herum."""
    
    elapsed_time, match = evaluate_regex_performance(pattern, text)
    
    print(f"Regex: {pattern}")
    print(f"Durchlaufzeit: {elapsed_time:.6f} seconds")
    print(f"Match found: {match is not None}")

if __name__ == "__main__":
    main()
