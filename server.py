from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import json
app = Flask(__name__)

current_id = 10

fabrics = {
    "velvet":{
        "id": 1,
        "fabric_name": "Velvet",
        "image": "https://images.fabric.com/images/1080/1080/0374391.jpg",
        "summary": ("Velvet is a soft, luxurious fabric that is characterized by a " +
                    "dense pile of evenly cut fibers that have a smooth nap. " +
                    "Velvet has a beautiful drape and a unique soft and shiny " +
                    "appearance due to the characteristics of the short pile fibers."),
        "price_per_yard": "29.99",
        "purchase_site": "https://www.moodfabrics.com/catalogsearch/result/index?q=velvet",
        "common_clothes": ["Evening gown", "Coat", "Zip-up Sweater"],
        "sewing_tips": ("Because of velvet’s surface texture, stitching lines tend to show." +
                    "Choose styles with minimal design details such as darts, seams," +
                    "buttonholes, and topstitching. Designs with simple lines and semifitted" +
                    "to loose-fitting styles best display velvet’s qualities. Gathers, soft" +
                    "folds, and drapey styles work better than those that are fitted and" +
                    "contoured."),
        "similar_fabrics": ["Wool", "Fleece"]
    },
    "silk":{
        "id": 2,
        "fabric_name": "Silk",
        "image": "https://s3.eu-west-2.amazonaws.com/files.sewport.com/fabrics-directory/everything-you-need-to-know-about-silk-fabric/Burnt%20Orange%20Stretch%20Silk%20Charmeuse.jpg",
        "summary": ("Silk is a natural fiber known for its luster, shine, strength, and " +
                    "durability, and it has a long trading history across the world. Silk is " + 
                    "the epitome of luxury due to its high cost to produce, soft feel, and " + 
                    "elegant appearance, and it is thus a popular textile in high-end and " +
                    "couture fashion design."),
        "price_per_yard": "69.99",
        "purchase_site": "https://www.moodfabrics.com/catalogsearch/result/index?q=silk",
        "common_clothes": ["Nightgown", "Robe"],
        "sewing_tips": ("Stitches must be straight, even and pass exactly along the seam" +
                    "line. Uneven curved stitches create bumps, distortions and imperfections" +
                    "of the seams."),
        "similar_fabrics": ["Crepe", "Sateen", "Chiffon"]
    },
    "corduroy":{
        "id": 3,
        "fabric_name": "Corduroy",
        "image": "https://i.etsystatic.com/7086259/r/il/7010e3/2808591714/il_fullxfull.2808591714_cc66.jpg",
        "summary": ("Corduroy fabric is a ridged material, made up of woven pile-cut yarn, " +
                    "which are cut into cords, or wales. These are the vertical ribs that " +
                    "give corduroy its unique texture, and the width of the wales on the " +
                    "fabric defines the texture of the garment."),
        "price_per_yard": "20.99",
        "purchase_site": "https://www.moodfabrics.com/catalogsearch/result/index?q=corduroy",
        "common_clothes": ["Trousers", "Jacket", "Bucket Hat", "Skirt", "Suspenders"],
        "sewing_tips": ("The pile on corduroy can squish up while you’re sewing and pressing" +
                    "it. To avoid this, lower the presser foot pressure (if your sewing machine" +
                    "lets you), and lower the thread tension slightly too. If you’re using a wider" +
                    "wale corduroy, such as jumbo cord, you can also lengthen the stitches to about" +
                    "3mm."),
        "similar_fabrics": ["Moleskin", "Flannel"]
    },
    "linen":{
        "id": 4,
        "fabric_name": "Linen",
        "image": "https://i.pinimg.com/originals/fb/2f/37/fb2f374339b38e53dacb252effcefd3a.jpg",
        "summary": ("Linen is best described a fabric that is made from very fine fibers, " +
                    "derived from the flax plant. These fibers are carefully extracted, spun " +
                    "into yarn, and then woven into long sheets of comfortable, durable fabric " +
                    "called linen fabric."),
        "price_per_yard": "31.99",
        "purchase_site": "https://www.moodfabrics.com/catalogsearch/result/index?q=linen",
        "common_clothes": ["Dress", "Apron", "Pants", "Suit", "Tablecloth"],
        "sewing_tips": ("Actually, linen is easy to sew; it does not slip or stretch when" +
                    "you are cutting it out or sewing a seam. However, linen is prone to" +
                    "shrinking and to fraying, so special care must be taken when preparing" +
                    "it for layout and when finishing seams."),
        "similar_fabrics": ["Cotton", "Polyester", "Hemp"]
    },
    "chiffon":{
        "id": 5,
        "fabric_name": "Chiffon",
        "image": "https://www.fabricdirect.com/wp-content/uploads/2020/05/chiffon-fabric-dusty-rose.jpg",
        "summary": ("From Bollywood to ball gowns, chiffon is a popular, decorative, " +
                    "lightweight fabric that was is associated with elegance and luxury. " +
                    "Chiffon’s shimmery and sheer appearance has proliferated in fashion " +
                    "and design for centuries."),
        "price_per_yard": "15.99",
        "purchase_site": "https://www.moodfabrics.com/catalogsearch/result/index?q=chiffon",
        "common_clothes": ["Blouse", "Summer dress", "Wedding dress", "Scarf", "Ribbon"],
        "sewing_tips": ("Sheer and lightweight fabric is known to get swallowed in the" +
                    "throat plate opening. Be sure you are using the smallest opening throat" +
                    "plate available for your machine."),
        "similar_fabrics": ["Crepe"]
    },
    "denim":{
        "id": 6,
        "fabric_name": "Denim",
        "image": "https://m.media-amazon.com/images/I/81Z1rSrJXNL._AC_SL1000_.jpg",
        "summary": ("Denim is a strong cotton fabric made using a twill weave, which " +
                    "creates a subtle diagonal ribbing pattern. The cotton twill fabric " +
                    "is warp-facing, meaning that the weft threads go under two or more warp " +
                    "threads, and the warp yarns are more prominent on the right side. The " +
                    "diagonal ribbing is what makes denim fabric different from canvas or " +
                    "cotton duck, which is also a sturdy woven cotton fabric."),
        "price_per_yard": "15.99",
        "purchase_site": "https://www.moodfabrics.com/catalogsearch/result/index?q=denim",
        "common_clothes": ["Jeans", "Denim Jacket", "Denim Skirt", "Shoes", "Suspenders"],
        "sewing_tips": ("Take your time sewing, hold the fabric as firmly as you can while" +
                    "feeding through the machine, do not push or pull.  If your sewing" +
                    "machine is having difficulties with a particularly bulky seam, you might" +
                    "want to use the handwheel.  It's pretty easy to break a needle when sewing" +
                    "denim, so be careful."),
        "similar_fabrics": ["Chambray", "Linen", "Hemp"]
    },
    "leather":{
        "id": 7,
        "fabric_name": "Leather",
        "image": "http://hautehousefabric.com/images/Product/large/3401.jpg",
        "summary": ("Leather is any fabric that is made from animal hides or skins. " +
                    "Different leathers result from different types of animals and " +
                    "different treatment techniques. While cowhide is the most popular " +
                    "type of animal skin used for leather, comprising about 65 percent of all " +
                    "leather produced, almost any animal can be made into leather, from crocodiles " +
                    "to pigs to stingrays. Leather is a durable, wrinkle-resistant fabric, and it can " +
                    "take on many different looks and feels based on the type of animal, grade, and treatment."),
        "price_per_yard": "65.99",
        "purchase_site": "https://www.leatherhidestore.com/",
        "common_clothes": ["Leather Jacket", "Wallet", "Belt", "Bag", "Gloves", "Boots"],
        "sewing_tips": ("Simply apply a line of tape between the two pieces of leather you" +
                    "want to sew, placing the tape along the edge of your leather, within" +
                    "what will be the seam allowance. Then sew your seam, and the tape will" +
                    "remain inside the seam allowance (no need to try to remove it). Believe" +
                    "it or not, this is a standard leather construction method, and if you" +
                    "could peek inside the seams of commercially-made leather goods, you would" +
                    "likely find tape or glue in the seam allowances."),
        "similar_fabrics": ["Vinyl", "Waxed Cotton", "Recycled Rubber"]
    },
    "lace":{
        "id": 8,
        "fabric_name": "Lace",
        "image": "https://cdn.onlinefabricstore.com/products/SLAC126_1.jpg",
        "summary": ("Lace is a delicate fabric made from yarn or thread, characterised by " +
                    "open designs and patterns created through a variety of different methods. " +
                    "Lace fabric was originally made from silk and linen, but today cotton " +
                    "thread and synthetic fibers are both used. Lace is a decorative fabric " +
                    "used to accent and embellish clothing and home decor items. Lace is " +
                    "traditionally considered a luxury textile, as it takes a lot of time and " +
                    "expertise to make."),
        "price_per_yard": "24.99",
        "purchase_site": "https://www.moodfabrics.com/fashion-fabrics/other-fabrics/lace",
        "common_clothes": ["Wedding Dress", "Shawl", "Scarf", "Accessories"],
        "sewing_tips": ("When you have your pieces ready to sew, start by stitching the" +
                    "lining to neaten areas like necklines. Turn the neatened necklines so" +
                    "the lining is on the inside of the garment. Trim closely to the" +
                    "stitching line."),
        "similar_fabrics": ["Eyelet", "Chiffon"]
    },
    "cashmere":{
        "id": 9,
        "fabric_name": "Cashmere",
        "image": "https://i.etsystatic.com/25720085/r/il/26505c/3294570215/il_570xN.3294570215_pbpn.jpg",
        "summary": ("Cashmere is one of the softest and most luxurious forms of wool, " +
                    "characterized by the fineness of the fibers, which are almost silky. " +
                    "It’s considered one of the most high-end fibers, as pure cashmere can " +
                    "be very expensive due to the involved production process, where the " +
                    "fibers are separated by hand from the molted coats of goats."),
        "price_per_yard": "199.99",
        "purchase_site": "https://www.moodfabrics.com/catalogsearch/result/index?q=cashmere",
        "common_clothes": ["Sweater", "Scarf", "Socks", "Thermal Wear", "Gloves", "Blazer"],
        "sewing_tips": ("Sew tautly but without stretching the fabric. Lift the fabric every" +
                    "6 inches and smooth it. Stabilize necklines and shoulder seams with stay" +
                    "tape or selvage strips."),
        "similar_fabrics": ["Wool", "Fleece"]
    },
    "rayon":{
        "id": 10,
        "fabric_name": "Rayon",
        "image": "https://i5.walmartimages.com/asr/2b1de833-7138-42a2-b8af-0dfefbf5342d_1.4f5a71d0ec7ee953c58ebeef691feed6.jpeg?odnHeight=612&odnWidth=612&odnBg=FFFFFF",
        "summary": ("Rayon is a semi-synthetic cellulosic fiber used widely in everything " +
                    "from clothing construction to bedsheets to tire cord. While rayon is " +
                    "made from natural materials (like beech trees or bamboo), it undergoes " +
                    "intense chemical processing, making it a manufactured fiber."),
        "price_per_yard": "16.99",
        "purchase_site": "https://www.moodfabrics.com/catalogsearch/result/index?q=rayon",
        "common_clothes": ["Athletic Wear", "Wrap Skirt", "Loose Blouse", "Summer Dress"],
        "sewing_tips": ("Because Rayon is a fiber type and not a weave, it’s difficult to" +
                    "give one-size-fits-all tips on sewing Rayon; after all, you wouldn’t" +
                    "sew a knit the same way you would sew a woven, or even a lawn the same" +
                    "way you would a twill!"),
        "similar_fabrics": ["Viscose"]
    }
}

resultfabs = []
resultids = []
resultsum = []
resultclothes = []

# ROUTES

@app.route('/')
def homepage():
    return render_template('homepage.html', fabrics=fabrics)   

@app.route('/view/<idnum>')
def view(idnum=None):
    global fabrics
    return render_template('view.html', fabrics=fabrics)

@app.route('/edit/<idn>')
def edit(idn=None):
    global fabrics
    return render_template('edit.html', fabrics=fabrics)

@app.route('/edit_fab', methods=['GET', 'POST'])
def edit_fab():
    global fabrics

    json_data = request.get_json()
    idDB = json_data["id"]
    fabricNameDB = json_data["fabric_name"]
    imgUrlDB = json_data["image"]
    fabricDescDB = json_data["summary"]
    pricePerYardDB = json_data["price_per_yard"]
    purchaseSiteDB = json_data["purchase_site"]
    commClothesDB = json_data["common_clothes"]
    sewTipsDB = json_data["sewing_tips"]
    simFabsDB = json_data["similar_fabrics"]

    # replace entry with edited information
    new_fabric_entry = {
        "id":  idDB,
        "fabric_name": fabricNameDB,
        "image": imgUrlDB,
        "summary": fabricDescDB,
        "price_per_yard": pricePerYardDB,
        "purchase_site": purchaseSiteDB,
        "common_clothes": commClothesDB,
        "sewing_tips": sewTipsDB,
        "similar_fabrics": simFabsDB
    }
    fabrics[fabricNameDB.lower()] = new_fabric_entry
    return jsonify(fabrics=fabrics)

@app.route('/add')
def add():
    return render_template('additem.html', fabrics=fabrics)

@app.route('/add_fabric', methods=['GET', 'POST'])
def add_fabric():
    global fabrics
    global current_id

    json_data = request.get_json()
    fabricNameDB = json_data["fabric_name"]
    imgUrlDB = json_data["image"]
    fabricDescDB = json_data["summary"]
    pricePerYardDB = json_data["price_per_yard"]
    purchaseSiteDB = json_data["purchase_site"]
    commClothesDB = json_data["common_clothes"]
    sewTipsDB = json_data["sewing_tips"]
    simFabsDB = json_data["similar_fabrics"]

    # add new entry to array with a new id
    current_id += 1
    new_id = current_id 
    new_fabric_entry = {
        "id":  current_id,
        "fabric_name": fabricNameDB,
        "image": imgUrlDB,
        "summary": fabricDescDB,
        "price_per_yard": pricePerYardDB,
        "purchase_site": purchaseSiteDB,
        "common_clothes": commClothesDB,
        "sewing_tips": sewTipsDB,
        "similar_fabrics": simFabsDB
    }
    fabrics[fabricNameDB.lower()] = new_fabric_entry
    return jsonify(fabrics=fabrics)

@app.route('/searchresults/<search>')
def searchresults(search=None):
    global fabrics
    global resultfabs
    global resultids

    resultfabs.clear()
    resultids.clear()
    resultsum.clear()
    resultclothes.clear()
    fabricfound = [value for key, value in fabrics.items() if search.lower() in key.lower()]
    
    # search through summaries
    for p_id, p_info in fabrics.items():    
        for key in p_info:
            if(key == "summary"):
                if(search.lower() in p_info[key].lower() and p_info not in fabricfound):
                    fabricfound.append(p_info)

    # search through common clothes
    for p_id, p_info in fabrics.items():    
        for key in p_info:
            if(key == "common_clothes"):
                for x in p_info[key]:
                    if(search.lower() in x.lower() and p_info not in fabricfound):
                        fabricfound.append(p_info)

    for dict in fabricfound:
        resultfabs.append((dict['fabric_name'])) 
        resultids.append(dict['id'])  
        resultsum.append(dict['summary'])
        resultclothes.append(dict['common_clothes'])   

    return render_template('searchresults.html', resultfabs=resultfabs, fabrics=fabrics, resultids=resultids, resultsum=resultsum, resultclothes=resultclothes)

if __name__ == '__main__':
   app.run(debug = True)