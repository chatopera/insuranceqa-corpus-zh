const _ = require('lodash')
const T = require('./translate')
const test = require('ava')
const jsonfile = require('jsonfile')
const path = require('path')

const sortByKeys = object => {
    const keys = Object.keys(object)
    const sortedKeys = _.sortBy(keys)

    return _.fromPairs(
        _.map(sortedKeys, key => [key, object[key]])
    )
}

function sleep(millseconds) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve()
        }, millseconds)
    })
}

function dump(file, obj) {
    return new Promise((resolve, reject) => {
        jsonfile.writeFile(file, obj, function (err) {
            if (err)
                return reject(err)
            resolve()
        })
    })
}

test.skip('process label2answer#', async (t) => {
    // const label2answer = require('../label2answer.json')
    const label2answer = require('../untraned.answers.json')
    var post = {}
    var untrans = {}
    var defer = 0
    for (let x of _.keys(label2answer)) {
        console.log(x)
        console.log('en', label2answer[x].text)
        let label = x;
        try {
            let translated = await T(label2answer[x].text);
            console.log('index:' + x + '<< translated:' + translated)
            post[label] = {
                zh: translated,
                en: label2answer[x].text
            }
            defer += 1
            // Google API limits
            // Characters per 100 seconds per user	100,000	
            if (defer % 10 == 0) {
                await sleep(2000)
                await dump(path.join(__dirname, '../label2answer.zh-CN.r2.json'), post)
                await dump(path.join(__dirname, '../label2answer.zh-CN.r2.untrans.json'), untrans)
            }
        } catch (e) {
            if (e.message === 'User Rate Limit Exceeded') {
                console.log('oops ..., User Rate Limit Exceeded, sleep ...')
                untrans[x] = {
                    en: label2answer[x].text
                }
                await sleep(10000)
                await dump(path.join(__dirname, '../label2answer.zh-CN.r2.untrans.json'), untrans)
                await dump(path.join(__dirname, '../label2answer.zh-CN.r2.json'), post)
            } else {
                console.log('not sure what happened.', e)
            }
        }
    }

    console.log('translate done.')
    await dump(path.join(__dirname, '../label2answer.zh-CN.r2.untrans.json'), untrans)
    await dump(path.join(__dirname, '../label2answer.zh-CN.r2.json'), post)
    console.log('dump done.')
    t.pass()
})

async function translate_job(data, file_basename) {
    var post = {}
    var untrans = {}
    var defer = 0
    for (let x of _.keys(data)) {
        console.log(x)
        console.log('value', data[x].question_en)
        let label = x;
        let tokens = data[x].tokens;
        try {
            let translated = await T(data[x]['question_en']);
            console.log('index:' + x + '<< translated:' + translated)
            post[label] = {
                zh: translated,
                ground_truth: data[x]['ground_truth'],
                pool: data[x]['pool']
            }
            defer += 1
            // Google API limits
            // Characters per 100 seconds per user	100,000	
            if (defer % 10 == 0) {
                await sleep(3500)
                await dump(file_basename + '.zh-CN.json', post)
            }
        } catch (e) {
            if (e.message === 'User Rate Limit Exceeded') {
                console.log('oops ..., User Rate Limit Exceeded, sleep ...')
                untrans[x] = {
                    en: data[x].question_en,
                    ground_truth: data[x]['ground_truth'],
                    pool: data[x]['pool']
                }
                await sleep(10000)
                await dump(file_basename + '.untrans.json', untrans)
                await dump(file_basename + '.zh-CN.json', post)
            } else {
                console.log('not sure what happened.', e)
            }
        }
    }
    console.log('translate done.')
    await dump(file_basename + '.untrans.json', untrans)
    await dump(file_basename + '.zh-CN.json', post)
    console.log('dump done.')
}

test.skip('process InsuranceQA.question.anslabel.raw', async (t) => {
    // "InsuranceQA.question.anslabel.raw.100.pool.solr.test.encoded.gz.json",
    // "InsuranceQA.question.anslabel.raw.100.pool.solr.train.encoded.gz.json",
    // "InsuranceQA.question.anslabel.raw.100.pool.solr.valid.encoded.gz.json",
    // "InsuranceQA.question.anslabel.raw.1000.pool.solr.test.encoded.gz.json",
    // "InsuranceQA.question.anslabel.raw.1000.pool.solr.train.encoded.gz.json",
    // "InsuranceQA.question.anslabel.raw.1000.pool.solr.valid.encoded.gz.json",
    // "InsuranceQA.question.anslabel.raw.1500.pool.solr.test.encoded.gz.json",
    // "InsuranceQA.question.anslabel.raw.1500.pool.solr.train.encoded.gz.json",
    // "InsuranceQA.question.anslabel.raw.1500.pool.solr.valid.encoded.gz.json",

    const raw_json = ["InsuranceQA.question.anslabel.raw.500.pool.solr.test.encoded.gz.json",
        "InsuranceQA.question.anslabel.raw.500.pool.solr.train.encoded.gz.json",
        "InsuranceQA.question.anslabel.raw.500.pool.solr.valid.encoded.gz.json"
    ]
    for (let x in raw_json) {
        console.log('Processing data ' + raw_json[x])
        let data = require('../tmp/' + raw_json[x])
        let file_path = path.join(__dirname, '../' + path.basename(raw_json[x]))
        await translate_job(data, file_path)
    }
    t.pass()
})

test.skip('process untrans InsuranceQA.label2answer', async (t) => {
    var data = require('../tmp/label2answer.zh-CN.201707252235.untrans.json')
    var result = {}

    for (let x in data) {
        let label = x;
        let tokens = data[x].tokens;
        console.log("data", x, data[x]['en'])
        var translated = await T(data[x]['en'])
        result[label] = {
            tokens: tokens,
            zh: translated
        }
    }
    console.log("data size", _.keys(data).length)
    await dump('file_basename' + '.zh-CN.json', result)
    t.pass()
})

test.skip('process merge InsuranceQA.label2answer', async (t) => {
    var pre = require('../corpus/answers.201707261842.json')
    console.log("data pre", _.keys(pre).length)
    var rc2 = require('../tmp/label2answer.zh-CN.r2.json')
    console.log("data rc2", _.keys(rc2).length)

    var rc3 = require('../tmp/label2answer.zh-CN.r3.json')
    console.log("data rc3", _.keys(rc3).length)

    var result = _.merge(pre, rc2);

    var result2 = _.merge(result, rc3)

    var result3 = sortByKeys(result2)
    console.log("data total", _.keys(result3).length)

    await dump('./corpus/answers.json', result3)
    t.pass()
})

test.skip('process trans answers on check', async (t) => {
    const predata = require('../question.anslabel/answers.201707261842.json')
    const data3 = require('../label2answer.json')
    var result = {}

    for (let x in data3) {
        if (predata[x]) {
            // pass
            // console.log('already translated.')
        } else {
            console.log('trans', x)
            result[x] = data3[x]

        }
    }

    console.log("all size", _.keys(data3).length)
    console.log('traned length', (_.keys(predata)).length)
    console.log('untranslated length', (_.keys(result)).length)
    await dump('untraned.answers' + '.zh-CN.json', sortByKeys(result))
    t.pass()
})

test.skip('combine questions en_US and zh_CN', async (t) => {
    const zh = require('../corpus/train.zh_CN.json')
    const en = require('../corpus/train.en_US.json')
    var result = {}

    if ((_.keys(zh)).length !== (_.keys(en)).length) {
        throw new Error('do not match.')
    }

    for (let x in zh) {
        result[x] = {
            zh: zh[x]['zh'].trim(),
            en: en[x]['question_en'].trim(),
            domain: en[x]['domain'],
            answers: en[x]['ground_truth'],
            pool: en[x]['pool']
        }
    }

    console.log("all size", _.keys(result).length)
    await dump('./corpus/train.json', sortByKeys(result))
    t.pass()
})

test.skip('validate answers', (t) => {
    const data = require('../corpus/answers.json')
    var result = {}

    for (let x in data) {
        console.log('index', x)
        t.is((_.keys(data[x])).length, 2, "should have 2 keys")
        t.truthy(data[x]['en'], "should have en")
        t.truthy(data[x]['zh'], "should have zh")
    }

    console.log("all size", _.keys(data).length)
    t.pass()
})


async function convertEviencesToPool(file) {
    var data = require(file);
    for (let x in data) {
        // console.log('index', x)
        data[x]['pool'] = data[x]['evidences']
        delete data[x]['evidences']
    }
    await dump(path.basename(file) + '.post.json', data)
}

test.skip('convert evidences to pool', async (t) => {
    const files = [
        '../corpus/valid.json',
        '../corpus/test.json',
        '../corpus/train.json'
    ]
    for (let x in files) {
        await convertEviencesToPool(files[x])
    }

    t.pass()
})

async function regenPoolData(target, pool_size) {
    var data = require(target.path);
    var source = require(target.retune)
    for (let x in data) {
        var spool = source[x]['pool']
        if (spool.length != 500) {
            throw new Error('Wrong length for spool.')
        }

        if (source[x]['question_en'].trim() != data[x]['en']) {
            throw new Error('Wrong info text for question.')
        }
        var tpool = []
        var answers = data[x]['answers']
        var index = 0
        while(tpool.length < pool_size){
            if(!_.includes(answers, spool[index])){
                tpool.push(spool[index])
            }
            index += 1;
        }
        data[x]['negatives'] = tpool;
        delete data[x]['pool']
    }
    await dump(path.basename(target.path) + '.repool.json', data)
}

test.skip('regen pool', async (t) => {
    const pool_size = 200
    const files = [
        {
            path: '../corpus/valid.json',
            retune: '../tmp/InsuranceQA.question.anslabel.raw.500.pool.solr.valid.encoded.gz.json'
        },
        {
            path: '../corpus/train.json',
            retune: '../tmp/InsuranceQA.question.anslabel.raw.500.pool.solr.train.encoded.gz.json'
        },
        {
            path: '../corpus/test.json',
            retune: '../tmp/InsuranceQA.question.anslabel.raw.500.pool.solr.test.encoded.gz.json'
        }
    ]

    for (let x in files) {
        await regenPoolData(files[x], pool_size)
    }

    t.pass()
})
