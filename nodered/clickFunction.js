const delay = (/** @type {number} */ ms) => new Promise(resolve => setTimeout(resolve, ms))
const clickArray = msg.clicks
for(let click of clickArray){
    const body = [null, null, null, null];
    body[click.dir === "up" ? 0 : 1] = {};
    for(let i=0; i < click.clicks; i++){
        node.send(body);
        delay(500);
    }
    node.send([null, null, {}, null])
    await delay(500)
}
//return msg;
return [null, null, null, {}];