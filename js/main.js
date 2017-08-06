const _ = require('lodash')
const T = require('./translate')
const test = require('ava')
const jsonfile = require('jsonfile')
const path = require('path')
const fs = require("fs");
const JSONStream = require("JSONStream");
const debug = require('debug')('insuranceqa-corpus-zh')
const readlineq = require('readlineq')

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

test.skip('1. process label2answer#', async (t) => {
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

test.skip('2. process InsuranceQA.question.anslabel.raw', async (t) => {
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

test.skip('3. process untrans InsuranceQA.label2answer', async (t) => {
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

test.skip('4. process merge InsuranceQA.label2answer', async (t) => {
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

test.skip('5. process trans answers on check', async (t) => {
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

test.skip('6. combine questions en_US and zh_CN', async (t) => {
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

test.skip('7. validate answers', (t) => {
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

test.skip('8. convert evidences to pool', async (t) => {
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
        while (tpool.length < pool_size) {
            if (!_.includes(answers, spool[index])) {
                tpool.push(spool[index])
            }
            index += 1;
        }
        data[x]['negatives'] = tpool;
        delete data[x]['pool']
    }
    await dump(path.basename(target.path) + '.repool.json', data)
}

test.skip('9. regen pool', async (t) => {
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
/**
 * Stop words, also contain punctuations
 */
async function load_stopped_words() {
    const file = './tmp/stopwords.txt'
    var lines = await readlineq(file)
    return lines
}

function map_tokens_to_ids(tokens, vocab, stopwords) {
    let ids = [];
    for (let y in tokens) {
        let [word, tag] = tokens[y].split('\t');
        if (word && tag) {
            // debug('word', word);
            // debug('tag', tag);
            if (!stopwords.includes(word)) { // not a stop word
                if (vocab.word2id[word]) {
                    ids.push(vocab.word2id[word])
                } else {
                    ids.push(0) // for UNK word
                }
            }
        }
    }
    return ids;
}

async function load_answers_collection() {
    const file = './tmp/iqa.answers.tokenlized';
    let data = {}
    let lines = await readlineq(file);
    for (let x in lines) {
        let [index, tokens] = lines[x].split("++$++")
        data[index.trim()] = tokens.trim()
    }
    return data;
}

function parse_raw_string_to_json(raw) {
    return JSON.parse(raw.replace(/(u)?'/g, '"'));
}

/**
 * Dump huge array to file
 * @param {*} to 
 * @param {*} obj 
 */
function dump_huge_array_to_file(to, obj) {
    return new Promise((resolve, reject) => {
        var records = obj
        var transformStream = JSONStream.stringify();
        var outputStream = fs.createWriteStream(to);
        transformStream.pipe(outputStream);
        records.forEach(transformStream.write);
        transformStream.end();

        outputStream.on(
            "finish",
            function handleFinish() {
                console.log("dump_huge_array_to_file done");
                resolve();
            }
        );
    });
}

test.only('10. gen pair data', async (t) => {
    const vocab = require('../tmp/iqa.vocab.json')
    const stopwords = await load_stopped_words()
    const answers_collection = await load_answers_collection()
    t.truthy(_.keys(answers_collection).length > 0, "wrong answers_collection")

    const files = {
        './tmp/iqa.test.tokenlized': '../tmp/iqa.test.tokenlized.pair.json',
        './tmp/iqa.valid.tokenlized': '../tmp/iqa.valid.tokenlized.pair.json',
        './tmp/iqa.train.tokenlized': '../tmp/iqa.train.tokenlized.pair.json'
    }

    const file_keys = _.keys(files);
    for (let t in file_keys) {
        let file_path = file_keys[t];
        let target_path = files[file_path];
        console.log('in:', file_path);
        console.log('output:', target_path);
        // const iqa_tokenlized_data = await readlineq('./tmp/iqa.train.tokenlized')
        const iqa_tokenlized_data = await readlineq(file_path)
        var pair_data = []
        for (let x in iqa_tokenlized_data) {
            let [index, question, answers_raw, negtives_raw] = iqa_tokenlized_data[x].split('++$++')
            index = index.trim()
            debug('index', index, 'question', question)
            let question_ids = map_tokens_to_ids(question.split(' '), vocab, stopwords)
            // debug('question_id', question_ids)
            // debug('index', index, 'answers string', answers_raw)
            // debug('index', index, 'raw ', raw)
            let answers = parse_raw_string_to_json(answers_raw)
            // debug('index', index, 'answers', answers)
            for (let o in answers) {
                let answer_ids = map_tokens_to_ids(answers_collection[answers[o]].split(' '), vocab, stopwords);
                debug('index', index, 'answer ids', JSON.stringify(answer_ids))
                pair_data.push({
                    qid: index,
                    question: question_ids,
                    utterance: answer_ids,
                    label: [1, 0] // label[0]: is answer, label[1]: is negative
                })
                // for every question, provide one correct answer
                if(o == 0){
                    break;
                }
            }
            let negtives = parse_raw_string_to_json(negtives_raw)
            debug('index', index, 'negatives', negtives)
            for (let o in negtives) {
                let negtive_ids = map_tokens_to_ids(answers_collection[negtives[o]].split(' '), vocab, stopwords);
                // debug('index', index, 'negtive ids', JSON.stringify(negtive_ids))
                pair_data.push({
                    qid: index,
                    question: question_ids,
                    utterance: negtive_ids,
                    label: [0, 1] // label[0]: is answer, label[1]: is negative                
                })
                // for every question, provide nine negtive answer
                if(o == 9){
                    break;
                }
            }
        }
        console.log(file_path, 'pair_data size', pair_data.length, 'saved ', path.join(__dirname, target_path))
        await dump_huge_array_to_file(path.join(__dirname, target_path), pair_data)
    }
    t.pass()
})