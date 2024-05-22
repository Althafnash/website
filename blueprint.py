from flask import Blueprint , render_template , redirect , url_for
import subprocess

def openAI():
    subprocess.call("I:/codeing/website/phython/PY_AI/AI.py")

Nashweb = Blueprint(__name__ , "Nashweb")

@Nashweb.route("/")
def WebsiteHome():
    return render_template("home.html" )

@Nashweb.route("/profile")
def WebsiteHome2():
    return render_template("homepage.html" )

@Nashweb.route("/Docs")
def WebsiteDocs():
    return render_template("docs.html" )

@Nashweb.route("/ICT/Opreating_system")
def OS():
    return render_template("./ICT/opreating_system.html" )

@Nashweb.route("/science/physics/Force")
def force():
    return render_template("./physics/Force.html" )

@Nashweb.route("/science/physics/Geometric_optics")
def light():
    return render_template("./physics/Geometric_optics.html" )

@Nashweb.route("/science/physics/motion")
def motion():
    return render_template("./physics/motion.html" )

@Nashweb.route("/about")
def about():
    return render_template("about.html" )

@Nashweb.route("/docs/science")
def docs():
    return render_template("./docs/science_docs.html" )

@Nashweb.route("/docs/history")
def history():
    return render_template("./docs/history_docs.html" )

@Nashweb.route("/docs/litreature")
def litreature():
    return render_template("./docs/litreature_docs.html" )

@Nashweb.route("/docs/english")
def english():
    return render_template("./docs/english.html" )

@Nashweb.route("/docs/ict")
def ict():
    return render_template("./docs/ict_docs.html" )

@Nashweb.route("/docs/Maths")
def Maths():
    return render_template("./docs/Maths_docs.html" )

@Nashweb.route("/science/physics")
def physics():
    return render_template("physics.html" )

@Nashweb.route("/science/biologhy")
def biologhy():
    return render_template("biologhy.html" )

@Nashweb.route("/science/chemistry")
def chemistry():
    return render_template("chemistry.html" )

@Nashweb.route("/ICT/programming/Javascript")
def javascript():
    return render_template("./javascript/javascript.html" )

@Nashweb.route("/ICT/programming/Javascript/Javascript_output")
def Javascript_output():
    return render_template("./javascript/javascript_output.html" )

@Nashweb.route("/ICT/programming/Javascript/syntax")
def javascript_syntax():
    return render_template("./javascript/javascript_syntax.html" )

@Nashweb.route("/ICT/programming/Javascript/variable")
def javascript_variable():
    return render_template("./javascript/javascript_variable.html" )

@Nashweb.route("/ICT/programming/Javascript/let")
def javascript_let():
    return render_template("./javascript/javascript_let.html" )

@Nashweb.route("/ICT/programming/Javascript/const")
def javascript_const():
    return render_template("./javascript/javascript_const.html" )

@Nashweb.route("/resource")
def help():
    return render_template("help.html" )

@Nashweb.route("/ICT/sdlc")
def sdlc():
    return render_template("./ICT/sdlc.html" )

@Nashweb.route("/ICT/genaration of computres")
def gen():
    return render_template("./ICT/gen.html" )

@Nashweb.route("/science/physics/preasure")
def preasure():
    return render_template("./physics/preasure.html" )

@Nashweb.route("/science/physics/Density")
def density():
    return render_template("./physics/density.html" )

@Nashweb.route("/science/physics/Friction")
def Friction():
    return render_template("./physics/friction.html" )

@Nashweb.route("/science/physics/Momeuntum_and_gravity")
def gravity():
    return render_template("./physics/gravity.html" )

@Nashweb.route("/science/physics/Newtons_laws")
def Newton():
    return render_template("./physics/newton.html" )

@Nashweb.route("/science/physics/simple_machines")
def machines():
    return render_template("./physics/machines.html" )

@Nashweb.route("/History/The_social_organization_of_ancient_soceity")
def soceity():
    return render_template("./History/soceity.html" )

@Nashweb.route("/History/The_Ancient_soceity_of_sri_lanka" )
def ancient():
    return render_template("./History/ancient_society.html" )

@Nashweb.route("/Biologhy/Classification_of_animals" )
def classification():
    return render_template("./biologhy/classification.html" )

@Nashweb.route("/The art of thinking clearly/home" )
def art():
    return render_template("/books/The art of thinking clearly/home.html" )

@Nashweb.route("/The art of thinking clearly/introducation" )
def art1():
    return render_template("/books/The art of thinking clearly/introducation.html")

@Nashweb.route("/The art of thinking clearly/survivorship_bias" )
def art2():
    return render_template("/books/The art of thinking clearly/survicorshipbias.html" )

@Nashweb.route("/The art of thinking clearly/swimmers_body_illusion" )
def art3():
    return render_template("/books/The art of thinking clearly/summiersbodyillusion.html" )

@Nashweb.route("/The art of thinking clearly/clustering_illusion" )
def art4():
    return render_template("/books/The art of thinking clearly/clustersillusion.html" )

@Nashweb.route("/The art of thinking clearly/social_proof" )
def art5():
    return render_template("/books/The art of thinking clearly/socialproof.html" )

@Nashweb.route("/The art of thinking clearly/sunk_cost_fallacy" )
def art6():
    return render_template("/books/The art of thinking clearly/sunkcostfallacy.html" )

@Nashweb.route("/The art of thinking clearly/Reciprocity" )
def art7():
    return render_template("/books/The art of thinking clearly/reposicty.html" )

@Nashweb.route("/The art of thinking clearly/Comformation bias" )
def art8():
    return render_template("/books/The art of thinking clearly/conformation.html" )

@Nashweb.route("/The art of thinking clearly/Authority bias" )
def art9():
    return render_template("/books/The art of thinking clearly/Authority.html" )

@Nashweb.route("/The art of thinking clearly/contrarst effect" )
def art10():
    return render_template("/books/The art of thinking clearly/contrast.html" )

@Nashweb.route("/search" )
def search():
    return render_template("/search.html" )
    
@Nashweb.route("/Dashboard" )
def dashboard():
    return render_template("/Dashboard.html" )

@Nashweb.route("/Science/Arrangements-of-particals" )
def particals():
    return render_template("Chemsitry/arrganments-of-particals.html" )

@Nashweb.route("/Science/Speration-Methods" )
def sperate():
    return render_template("Chemsitry/speration.html" )

@Nashweb.route("/Science/Atoms" )
def atoms():
    return render_template("Chemsitry/atoms.html" )

@Nashweb.route("/Science/Chromotography" )
def chromotor():
    return render_template("Chemsitry/chromoto.html" )

@Nashweb.route("/Science/metals" )
def metals():
    return render_template("Chemsitry/metals.html" )

@Nashweb.route("/Science/nonmetals" )
def non():
    return render_template("Chemsitry/non-metals.html" )

@Nashweb.route("/Book_summaries")
def books():
    return render_template("books/book_summaries.html")

@Nashweb.route("/Book_summaries/Laws")
def bookslaw():
    return render_template("books/laws.html")

@Nashweb.route("/Book_summaries/The art of thinking clearly/home")
def bookssptite():
    return render_template("/books/The art of thinking clearly/home.html")

