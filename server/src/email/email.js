const nodemailer = require('nodemailer');
const fs = require('fs');
const util = require('util');
const readFile = util.promisify(fs.readFile);

class Email {
  constructor() {
    this.transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        user: 'your-email@gmail.com',
        pass: 'your-password',
      },
    });
  }

  /**
   * 
   * @param { who email is being sent to } to 
   * @param { subject of the email } subject 
   * @param { the name of the html being rendered with templateData } templateName 
   * @param { what's going to be rendered in the templateName } templateData 
   * @param { default path of the html being rendered } defaultPath
   */
  async sendEmail(to, subject, templateName, templateData, defaultPath="../templates") {
    const template  = await readFile(`${defaultPath}/${templateName}.html`, 'utf8');
    const html      = this.renderTemplate(template, templateData);

    const mailOptions = {
      from: 'Your Name <your-email@gmail.com>',
      to,
      subject,
      html,
    };
    this.transporter.sendMail(mailOptions, (error, info) => {
      if (error) {
        console.error(error);
      } else {
        console.log(`Email sent: ${info.response}`);
      }
    });
  }

  /**
   * 
   * @param { html document to be rendered } template 
   * @param { data being rendered in the template } data 
   * @returns the rendered html with data
   */
  renderTemplate(template, data) { 
    let html = template;
    for (const key in data) {
      const value = data[key];
      const regex = new RegExp(`{{${key}}}`, 'g');
      html = html.replace(regex, value);
    }
    return html;
  }
}

module.exports = Email;