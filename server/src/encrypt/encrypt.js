const crypto = require('crypto');
const util = require("../util/util");


class Encryption {
  constructor(key) {
    this.key       = key;
    this.algorithm = 'aes-256-cbc';
  }

  /**
   * 
   * @param { what's being encrypted } data 
   * @returns string version of data encrypted
   */
  encrypt(data) {
    const iv        = crypto.randomBytes(16);
    const cipher    = crypto.createCipheriv(this.algorithm, Buffer.from(this.key), iv);
    let encrypted   = cipher.update(data);
    encrypted       = Buffer.concat([encrypted, cipher.final()]);
    // return iv.toString('hex') + ':' + encrypted.toString('hex');
    return `${iv.toString('hex')}:${encrypted.toString('hex')}`;
  }

  /**
   * 
   * @param { what's encrypted to decrypt } data 
   * @returns decrypted version of data
   */
  decrypt(data) {
    const parts         = data.split(':');
    const iv            = Buffer.from(parts.shift(), 'hex');
    const encryptedText = Buffer.from(parts.join(':'), 'hex');
    const decipher      = crypto.createDecipheriv(this.algorithm, Buffer.from(this.key), iv);
    let decrypted       = decipher.update(encryptedText);
    decrypted           = Buffer.concat([decrypted, decipher.final()]);
    return decrypted.toString();
  }
}

module.exports = Encryption;
