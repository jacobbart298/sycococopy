// Generated from c:\Users\User\OneDrive\Documenten\Open Universiteit\IB9902 Voorbereiden Afstuderen\gitwerk\sycococopy\src\core\Pythonic.g4 by ANTLR 4.9.2

from antlr_denter.DenterHelper import DenterHelper
from PythonicParser import PythonicParser

import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class PythonicLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PROTOCOL=1, ROLES=2, CLOSEBRKT=3, TO=4, FROM=5, SEND=6, SEQUENCE=7, SHUFFLE=8, 
		CHOICE=9, CLOSE=10, WORD=11, WS=12, NL=13;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"PROTOCOL", "ROLES", "CLOSEBRKT", "TO", "FROM", "SEND", "SEQUENCE", "SHUFFLE", 
			"CHOICE", "CLOSE", "WORD", "WS", "NL"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'protocol('", "'roles:'", "'):'", "'to'", "'from'", "'send'", 
			"'sequence:'", "'shuffle:'", "'choice:'", "'close'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PROTOCOL", "ROLES", "CLOSEBRKT", "TO", "FROM", "SEND", "SEQUENCE", 
			"SHUFFLE", "CHOICE", "CLOSE", "WORD", "WS", "NL"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	class MyCoolDenter(DenterHelper):
	    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
	        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
	        self.lexer: PythonicLexer = lexer

	    def pull_token(self):
	        return super(PythonicLexer, self.lexer).nextToken()

	denter = None

	def nextToken(self):
	    if not self.denter:
	        self.denter = self.MyCoolDenter(self, self.NL, PythonicParser.INDENT, PythonicParser.DEDENT, False)
	    return self.denter.next_token()



	public PythonicLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Pythonic.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17r\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3"+
		"\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13"+
		"\3\13\3\13\3\13\3\13\3\f\6\fa\n\f\r\f\16\fb\3\r\3\r\3\r\3\r\3\16\5\16"+
		"j\n\16\3\16\3\16\7\16n\n\16\f\16\16\16q\13\16\2\2\17\3\3\5\4\7\5\t\6\13"+
		"\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\3\2\3\6\2\62;C\\aac|\2t\2"+
		"\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2"+
		"\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2"+
		"\31\3\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5\'\3\2\2\2\7.\3\2\2\2\t\61\3\2"+
		"\2\2\13\64\3\2\2\2\r9\3\2\2\2\17>\3\2\2\2\21H\3\2\2\2\23Q\3\2\2\2\25Y"+
		"\3\2\2\2\27`\3\2\2\2\31d\3\2\2\2\33i\3\2\2\2\35\36\7r\2\2\36\37\7t\2\2"+
		"\37 \7q\2\2 !\7v\2\2!\"\7q\2\2\"#\7e\2\2#$\7q\2\2$%\7n\2\2%&\7*\2\2&\4"+
		"\3\2\2\2\'(\7t\2\2()\7q\2\2)*\7n\2\2*+\7g\2\2+,\7u\2\2,-\7<\2\2-\6\3\2"+
		"\2\2./\7+\2\2/\60\7<\2\2\60\b\3\2\2\2\61\62\7v\2\2\62\63\7q\2\2\63\n\3"+
		"\2\2\2\64\65\7h\2\2\65\66\7t\2\2\66\67\7q\2\2\678\7o\2\28\f\3\2\2\29:"+
		"\7u\2\2:;\7g\2\2;<\7p\2\2<=\7f\2\2=\16\3\2\2\2>?\7u\2\2?@\7g\2\2@A\7s"+
		"\2\2AB\7w\2\2BC\7g\2\2CD\7p\2\2DE\7e\2\2EF\7g\2\2FG\7<\2\2G\20\3\2\2\2"+
		"HI\7u\2\2IJ\7j\2\2JK\7w\2\2KL\7h\2\2LM\7h\2\2MN\7n\2\2NO\7g\2\2OP\7<\2"+
		"\2P\22\3\2\2\2QR\7e\2\2RS\7j\2\2ST\7q\2\2TU\7k\2\2UV\7e\2\2VW\7g\2\2W"+
		"X\7<\2\2X\24\3\2\2\2YZ\7e\2\2Z[\7n\2\2[\\\7q\2\2\\]\7u\2\2]^\7g\2\2^\26"+
		"\3\2\2\2_a\t\2\2\2`_\3\2\2\2ab\3\2\2\2b`\3\2\2\2bc\3\2\2\2c\30\3\2\2\2"+
		"de\7\"\2\2ef\3\2\2\2fg\b\r\2\2g\32\3\2\2\2hj\7\17\2\2ih\3\2\2\2ij\3\2"+
		"\2\2jk\3\2\2\2ko\7\f\2\2ln\7\"\2\2ml\3\2\2\2nq\3\2\2\2om\3\2\2\2op\3\2"+
		"\2\2p\34\3\2\2\2qo\3\2\2\2\7\2`bio\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}