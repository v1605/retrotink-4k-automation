const delay = (/** @type {number} */ ms) => new Promise(resolve => setTimeout(resolve, ms))
const clickArray = msg.clicks
for(let click of clickArray){
    const body = [null, null, null, null];
    body[click.dir === "up" ? 0 : 1] = {};
    for(let i=0; i < click.clicks; i++){
        node.send(body);
        await delay(500);
    }
    await delay(800);
    node.send([null, null, {}, null])
    await delay(500)
}
return [null, null, null, {}];